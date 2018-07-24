from thread_crawler import thread_crawl
from mongo_cache import Mongocache
from alexa_cb import AlexaCallback

def main(max_threads):
    scrape_Callback = AlexaCallback()
    cache = Mongocache()
    thread_crawl(scrape_Callback.seed_url, scrape_callback=scrape_Callback, cache=cache, max_threads=max_threads)

if __name__ == '__main__':
    main(20)