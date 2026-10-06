package storage

import (
	"bufio"
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"syscall"

	"github.com/vietvudanh/vietlott-data/crawler/internal/model"
)

type storedDraw struct {
	id   int
	data []byte
}

// LoadExistingDrawIDs reads a JSONL draw file and returns its numeric IDs,
// highest ID, and number of valid rows.
func LoadExistingDrawIDs(path string) (map[int]struct{}, int, int, error) {
	file, err := os.Open(path)
	if errors.Is(err, os.ErrNotExist) {
		return map[int]struct{}{}, 0, 0, nil
	}
	if err != nil {
		return nil, 0, 0, err
	}
	defer file.Close()

	ids := make(map[int]struct{})
	highestID, validRows := 0, 0
	scanner := bufio.NewScanner(file)
	scanner.Buffer(make([]byte, 64*1024), 16*1024*1024)
	scanner.Split(scanLinesPreserveCR)
	line := 0
	for scanner.Scan() {
		line++
		raw := append([]byte(nil), scanner.Bytes()...)
		data := bytes.TrimSpace(raw)
		if len(data) == 0 {
			continue
		}
		id, err := drawID(data)
		if err != nil {
			return nil, 0, 0, fmt.Errorf("%s:%d: %w", path, line, err)
		}
		ids[id] = struct{}{}
		validRows++
		if validRows == 1 || id > highestID {
			highestID = id
		}
	}
	if err := scanner.Err(); err != nil {
		return nil, 0, 0, err
	}
	return ids, highestID, validRows, nil
}

// AppendDrawsAtomic appends new draws, deduplicates by numeric ID, and rewrites
// path using compact JSONL. Existing rows retain their order; new rows are
// sorted numerically and written after existing rows. The original file is
// untouched if any read, marshal, or write operation fails.
func AppendDrawsAtomic(path string, draws []model.Draw) error {
	if len(draws) == 0 {
		return nil
	}

	pendingByID := make(map[int]storedDraw, len(draws))
	for _, draw := range draws {
		if draw == nil {
			return errors.New("cannot append nil draw")
		}
		data, err := json.Marshal(draw)
		if err != nil {
			return fmt.Errorf("marshal draw %q: %w", draw.GetID(), err)
		}
		data = bytes.TrimSpace(data)
		id, err := drawID(data)
		if err != nil {
			return fmt.Errorf("draw %q: %w", draw.GetID(), err)
		}
		if _, ok := pendingByID[id]; ok {
			continue
		}
		pendingByID[id] = storedDraw{id: id, data: data}
	}
	pending := make([]storedDraw, 0, len(pendingByID))
	for _, record := range pendingByID {
		pending = append(pending, record)
	}
	sort.SliceStable(pending, func(i, j int) bool { return pending[i].id < pending[j].id })

	dir := filepath.Dir(path)
	temp, err := os.CreateTemp(dir, "."+filepath.Base(path)+".tmp-*")
	if err != nil {
		return err
	}
	tempName := temp.Name()
	defer os.Remove(tempName)
	mode := os.FileMode(0o644)
	if info, statErr := os.Stat(path); statErr == nil {
		mode = info.Mode().Perm()
	} else if !errors.Is(statErr, os.ErrNotExist) {
		_ = temp.Close()
		return statErr
	}
	if err := temp.Chmod(mode); err != nil {
		_ = temp.Close()
		return err
	}

	writer := bufio.NewWriter(temp)
	file, err := os.Open(path)
	if errors.Is(err, os.ErrNotExist) {
		file = nil
	} else if err != nil {
		_ = temp.Close()
		return err
	}
	if file != nil {
		defer func() {
			if file != nil {
				_ = file.Close()
			}
		}()
		scanner := bufio.NewScanner(file)
		scanner.Buffer(make([]byte, 64*1024), 16*1024*1024)
		scanner.Split(scanLinesPreserveCR)
		existingIDs := make(map[int]struct{})
		line := 0
		for scanner.Scan() {
			line++
			raw := append([]byte(nil), scanner.Bytes()...)
			data := bytes.TrimSpace(raw)
			if len(data) == 0 {
				continue
			}
			id, err := drawID(data)
			if err != nil {
				_ = temp.Close()
				return fmt.Errorf("%s:%d: %w", path, line, err)
			}
			if _, ok := existingIDs[id]; ok {
				continue
			}
			existingIDs[id] = struct{}{}
			delete(pendingByID, id)
			if err := writeRecord(writer, storedDraw{id: id, data: raw}); err != nil {
				_ = temp.Close()
				return err
			}
		}
		if err := scanner.Err(); err != nil {
			_ = temp.Close()
			return err
		}
		if err := file.Close(); err != nil {
			return fmt.Errorf("close input %s: %w", path, err)
		}
		file = nil
	}
	pending = pending[:0]
	for _, record := range pendingByID {
		pending = append(pending, record)
	}
	sort.SliceStable(pending, func(i, j int) bool { return pending[i].id < pending[j].id })
	for _, record := range pending {
		if err := writeRecord(writer, record); err != nil {
			_ = temp.Close()
			return err
		}
	}
	if err := writer.Flush(); err != nil {
		_ = temp.Close()
		return err
	}
	if err := temp.Sync(); err != nil {
		_ = temp.Close()
		return err
	}
	if err := temp.Close(); err != nil {
		return err
	}
	if err := os.Rename(tempName, path); err != nil {
		return err
	}
	dirFile, err := os.Open(dir)
	if err != nil {
		return fmt.Errorf("target replaced but directory sync unavailable: %w", err)
	}
	defer dirFile.Close()
	if err := dirFile.Sync(); err != nil {
		if errors.Is(err, syscall.EINVAL) || errors.Is(err, syscall.ENOTSUP) {
			return fmt.Errorf("target replaced; directory sync unsupported: %w", err)
		}
		return fmt.Errorf("target replaced but directory sync failed: %w", err)
	}
	return nil
}

func writeRecord(writer *bufio.Writer, record storedDraw) error {
	if _, err := writer.Write(record.data); err != nil {
		return err
	}
	return writer.WriteByte('\n')
}

func scanLinesPreserveCR(data []byte, atEOF bool) (advance int, token []byte, err error) {
	if index := bytes.IndexByte(data, '\n'); index >= 0 {
		return index + 1, data[:index], nil
	}
	if atEOF && len(data) > 0 {
		return len(data), data, nil
	}
	return 0, nil, nil
}

func drawID(data []byte) (int, error) {
	var value struct {
		ID string `json:"id"`
	}
	if err := json.Unmarshal(data, &value); err != nil {
		return 0, fmt.Errorf("invalid JSON: %w", err)
	}
	raw := strings.TrimPrefix(value.ID, "#")
	if raw == "" {
		return 0, errors.New("draw ID is empty")
	}
	for _, char := range raw {
		if char < '0' || char > '9' {
			return 0, fmt.Errorf("draw ID %q is not numeric", value.ID)
		}
	}
	id, err := strconv.Atoi(raw)
	if err != nil {
		return 0, fmt.Errorf("draw ID %q is out of range: %w", value.ID, err)
	}
	return id, nil
}
