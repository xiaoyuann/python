from link_crawler import link_crawl
from mongo_cache import Mongocache


def main():
    cache = Mongocache()
    link_crawl('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip', cache=cache)

if __name__ == '__main__':
    main()