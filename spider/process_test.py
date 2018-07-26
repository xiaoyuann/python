import sys
from process_crawler import process_crawler
from mongo_cache import Mongocache
from alexa_cb import AlexaCallback


def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = Mongocache()
    cache.clear()
    process_crawler(scrape_callback.seed_url, max_threads=max_threads, scrape_callback=scrape_callback, cache=cache,)


if __name__ == '__main__':
    max_threads = 5
    main(max_threads)