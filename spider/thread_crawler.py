#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'


import time
import threading
from urllib.parse import urljoin, urlparse, urldefrag
import urllib.robotparser
from downloader import Downloader

SLEEP_TIME = 1

def thread_crawl(seed_url, max_threads=10, link_regex=None, delay=5, max_depth=-1, max_urls=-1, user_agent='Aurora-Twinkle', proxies=None, max_retries=1, scrape_callback=None, cache=None):
    crawl_queue = [seed_url]
    seen = set([seed_url])
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
                                if link not in seen:
                                    seen.add(link)
                                    crawl_queue.append(link)
                else:
                    print('user_agent: "' + user_agent + '" Blocked by robots.txt:', url)
    threads = []
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)


        while len(threads) < max_threads and crawl_queue:
            thread = threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
           
        time.sleep(SLEEP_TIME)

def get_robots(url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(url, '/robots.txt'))
    rp.read()
    return rp

def format_link(seed_url, link):
    link, _ = urldefrag(link)
    return urljoin(seed_url, link)

