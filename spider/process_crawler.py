#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'


import time
import threading
import multiprocessing
from mongo_queue import MongoQueue
from mongo_cache import Mongocache
from urllib.parse import urljoin, urldefrag
import urllib.robotparser
from downloader import Downloader

SLEEP_TIME = 1

def thread_crawl(seed_url, max_threads=10, delay=5, user_agent='Aurora-Twinkle', proxies=None, max_retries=1, scrape_callback=None, cache=None):
    crawl_queue = MongoQueue()
    crawl_queue.clear()
    crawl_queue.push(seed_url)
    D = Downloader(delay=delay, user_agent=user_agent, proxies=proxies, max_retries=max_retries, cache=cache)
    rp = get_robots(seed_url)

    def process_queue():
        while True:
            try:
                url = crawl_queue.pop()
            except IndexError:
                break
            else:
                if rp.can_fetch(user_agent, url):
                    html = D(url)
                    if scrape_callback:
                        try:
                            links = scrape_callback(url, html) or []
                        except Exception as e:
                            print("Error in callback for :{}:{}".format(url, e))
                        else:
                            for link in links:
                                link = format_link(seed_url, link)
                                crawl_queue.push(link)
                    crawl_queue.complete(url)
                else:
                    print('user_agent: "' + user_agent + '" Blocked by robots.txt:', url)

    threads = []
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)


        while len(threads) < max_threads and crawl_queue.peek():
            thread = threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)

        time.sleep(SLEEP_TIME)

def process_crawler(args, **kwargs):
    num_cpus = multiprocessing.cpu_count()
    print("Starting {} processes".format(num_cpus))
    processes = []
    for i in range(num_cpus):
        p = multiprocessing.Process(target=thread_crawl, args=[args], kwargs=kwargs)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

def get_robots(url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(url, '/robots.txt'))
    rp.read()
    return rp

def format_link(seed_url, link):
    link, _ = urldefrag(link)
    return urljoin(seed_url, link)

