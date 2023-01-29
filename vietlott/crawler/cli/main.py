import argparse

from vietlott.crawler.logger import congig_logging
from vietlott.crawler.products import power655

parser = argparse.ArgumentParser('vietlott app')
parser.add_argument('--product', type=lambda x: x if x in {'power655'} else None, help='product to crawl')
parser.add_argument('--pages', type=int, default=1, help='pages to crawl')
args = parser.parse_args()

if __name__ == '__main__':
    print(args)
    congig_logging()
    if args.product == 'power655':
        power655.crawl(args.pages)
    else:
        print('wrong product')
