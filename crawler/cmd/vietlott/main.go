package main

import (
	"context"
	"errors"
	"flag"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/vietvudanh/vietlott-data/crawler/internal/client"
	"github.com/vietvudanh/vietlott-data/crawler/internal/crawler"
	"github.com/vietvudanh/vietlott-data/crawler/internal/model"
	"github.com/vietvudanh/vietlott-data/crawler/internal/storage"
)

type options struct {
	command  string
	root     string
	product  string
	all      bool
	maxDraws int
}

type adapterFactory func(model.ProductName) (crawler.ProductAdapter, error)

var allProducts = []model.ProductName{
	model.Power655, model.Power645, model.Power535, model.Keno,
	model.Bingo18, model.Max3D, model.Max3DPro,
}

func main() {
	os.Exit(run(context.Background(), os.Args[1:], os.Stdout, os.Stderr, nil))
}

func run(ctx context.Context, args []string, stdout, stderr io.Writer, factory adapterFactory) int {
	opts, err := parseArgs(args)
	if err != nil {
		fmt.Fprintln(stderr, "error:", err)
		return 2
	}
	root, err := resolveRoot(opts.root)
	if err != nil {
		fmt.Fprintln(stderr, "error:", err)
		return 2
	}
	if factory == nil {
		c := client.NewClient()
		factory = func(name model.ProductName) (crawler.ProductAdapter, error) {
			return client.NewProductAdapter(c, name)
		}
	}
	switch opts.command {
	case "status":
		return status(ctx, root, stdout, stderr, factory)
	case "missing":
		return missing(ctx, root, opts, stdout, stderr, factory)
	case "sync":
		return syncProducts(ctx, root, opts, stdout, stderr, factory)
	default:
		fmt.Fprintln(stderr, "error: command is required (status, missing, or sync)")
		return 2
	}
}

func parseArgs(args []string) (options, error) {
	var opts options
	clean := make([]string, 0, len(args))
	for i := 0; i < len(args); i++ {
		if args[i] == "--root" {
			if i+1 == len(args) {
				return opts, errors.New("--root requires a path")
			}
			opts.root = args[i+1]
			i++
			continue
		}
		if strings.HasPrefix(args[i], "--root=") {
			opts.root = strings.TrimPrefix(args[i], "--root=")
			if opts.root == "" {
				return opts, errors.New("--root requires a path")
			}
			continue
		}
		clean = append(clean, args[i])
	}
	if len(clean) == 0 {
		return opts, errors.New("command is required (status, missing, or sync)")
	}
	opts.command = clean[0]
	if opts.command != "status" && opts.command != "missing" && opts.command != "sync" {
		return opts, fmt.Errorf("unknown command %q", opts.command)
	}
	fs := flag.NewFlagSet(opts.command, flag.ContinueOnError)
	fs.SetOutput(io.Discard)
	product := fs.String("product", "", "product name")
	all := fs.Bool("all", false, "all products")
	maxDraws := fs.Int("max-draws", 0, "maximum missing draws")
	if err := fs.Parse(clean[1:]); err != nil {
		return opts, err
	}
	if fs.NArg() != 0 {
		return opts, fmt.Errorf("unexpected argument %q", fs.Arg(0))
	}
	opts.product, opts.all, opts.maxDraws = *product, *all, *maxDraws
	if opts.maxDraws < 0 {
		return opts, errors.New("max-draws must be nonnegative")
	}
	if opts.command == "status" {
		if opts.product != "" || opts.all || opts.maxDraws != 0 {
			return opts, errors.New("status does not accept product, all, or max-draws")
		}
		return opts, nil
	}
	if opts.command == "missing" && opts.maxDraws != 0 {
		return opts, errors.New("missing does not accept max-draws")
	}
	if opts.product != "" {
		if _, err := model.Lookup(opts.product); err != nil {
			return opts, err
		}
	}
	if opts.command == "missing" && (opts.product == "" || opts.all) {
		return opts, errors.New("product is required and --all is not supported")
	}
	if opts.command == "sync" && ((opts.product == "" && !opts.all) || (opts.product != "" && opts.all)) {
		return opts, errors.New("exactly one of --product or --all is required")
	}
	return opts, nil
}

func resolveRoot(explicit string) (string, error) {
	candidates := []string{}
	if explicit != "" {
		candidates = append(candidates, explicit)
	} else {
		if cwd, err := os.Getwd(); err == nil {
			candidates = append(candidates, cwd)
		}
		if exe, err := os.Executable(); err == nil {
			candidates = append(candidates, filepath.Dir(exe))
		}
	}
	seen := map[string]struct{}{}
	for _, candidate := range candidates {
		path, err := filepath.Abs(candidate)
		if err != nil {
			continue
		}
		for {
			if _, ok := seen[path]; !ok {
				seen[path] = struct{}{}
				if isRoot(path) {
					return path, nil
				}
			}
			next := filepath.Dir(path)
			if next == path {
				break
			}
			path = next
		}
	}
	return "", errors.New("could not find repository root containing data/ and crawler/")
}

func isRoot(path string) bool {
	data, dataErr := os.Stat(filepath.Join(path, "data"))
	crawlerDir, crawlerErr := os.Stat(filepath.Join(path, "crawler"))
	return dataErr == nil && crawlerErr == nil && data.IsDir() && crawlerDir.IsDir()
}

func status(ctx context.Context, root string, out, errOut io.Writer, factory adapterFactory) int {
	exitCode := 0
	for _, name := range allProducts {
		product, _ := model.Lookup(string(name))
		adapter, err := factory(name)
		if err != nil {
			fmt.Fprintf(errOut, "error: %s: %v\n", name, err)
			fmt.Fprintf(out, "%s existing=0 latest=0 missing=0 written=0 failed=1\n", name)
			exitCode = 1
			continue
		}
		ids, _, existing, err := storage.LoadExistingDrawIDs(filepath.Join(root, "data", product.FileName))
		if err != nil {
			fmt.Fprintf(errOut, "error: %s: %v\n", name, err)
			fmt.Fprintf(out, "%s existing=0 latest=0 missing=0 written=0 failed=1\n", name)
			exitCode = 1
			continue
		}
		latest, err := adapter.Latest(ctx)
		if err != nil {
			fmt.Fprintf(errOut, "error: %s: latest: %v\n", name, err)
			fmt.Fprintf(out, "%s existing=%d latest=0 missing=0 written=0 failed=1\n", name, existing)
			exitCode = 1
			continue
		}
		missing := crawler.MissingIDs(ids, product.MinID, latest, 0)
		fmt.Fprintf(out, "%s existing=%d latest=%d missing=%d written=0 failed=0\n", name, existing, latest, len(missing))
	}
	return exitCode
}

func missing(ctx context.Context, root string, opts options, out, errOut io.Writer, factory adapterFactory) int {
	product, _ := model.Lookup(opts.product)
	adapter, err := factory(product.Name)
	if err != nil {
		fmt.Fprintln(errOut, "error:", err)
		return 1
	}
	ids, existing, latest, err := findMissing(ctx, root, product, adapter)
	if err != nil {
		fmt.Fprintln(errOut, "error:", err)
		return 1
	}
	fmt.Fprintf(out, "%s existing=%d latest=%d missing=%d written=0 failed=0\n", product.Name, existing, latest, len(ids))
	if len(ids) > 0 {
		fmt.Fprintf(out, "missing_ids=%s\n", joinIDs(ids))
	}
	return 0
}

func syncProducts(ctx context.Context, root string, opts options, out, errOut io.Writer, factory adapterFactory) int {
	names := allProducts
	if !opts.all {
		names = []model.ProductName{model.ProductName(opts.product)}
	}
	exitCode := 0
	for _, name := range names {
		product, _ := model.Lookup(string(name))
		adapter, err := factory(name)
		if err != nil {
			fmt.Fprintf(errOut, "error: %s: %v\n", name, err)
			exitCode = 1
			continue
		}
		report, syncErr := crawler.Sync(ctx, root, product, adapter, opts.maxDraws)
		fmt.Fprintf(out, "%s existing=%d latest=%d missing=%d written=%d failed=%d\n",
			report.Product, report.Existing, report.Latest, report.Missing, report.Written, len(report.FailedIDs))
		if syncErr != nil {
			fmt.Fprintf(errOut, "error: %s: %v\n", name, syncErr)
			exitCode = 1
		}
	}
	return exitCode
}

func findMissing(ctx context.Context, root string, product model.Product, adapter crawler.ProductAdapter) ([]int, int, int, error) {
	ids, _, existing, err := storage.LoadExistingDrawIDs(filepath.Join(root, "data", product.FileName))
	if err != nil {
		return nil, 0, 0, fmt.Errorf("load %s: %w", product.Name, err)
	}
	latest, err := adapter.Latest(ctx)
	if err != nil {
		return nil, existing, 0, fmt.Errorf("latest %s: %w", product.Name, err)
	}
	return crawler.MissingIDs(ids, product.MinID, latest, 0), existing, latest, nil
}

func joinIDs(ids []int) string {
	values := make([]string, len(ids))
	for i, id := range ids {
		values[i] = fmt.Sprint(id)
	}
	return strings.Join(values, ",")
}
