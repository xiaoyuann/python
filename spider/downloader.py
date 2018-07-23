#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import requests
from urllib.parse import urlparse
from datetime import datetime
import time
import random

DEFAULT_AGENT = 'Aurora-Twinkle'
DEFAULT_DELAY = 5
DEFAULT_RETRIES = 4
DEFAULT_TIMEOUT = 30

class Downloader:
    def __init__(self, delay=DEFAULT_DELAY, user_agent=DEFAULT_AGENT, proxies=None, max_retries=DEFAULT_RETRIES, cache=None):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.max_retries = max_retries
        self.cache = cache

    def __call__(self, url):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass

        if result is None:
            self.throttle.wait(url)
            proxies = random.choice(self.proxies) if self.proxies else None
            headers = {'User-agent': self.user_agent}
            result = self.download(url, headers, proxies=proxies, max_retries = self.max_retries)
            if self.cache:
                self.cache[url] = result
        return result['html']

    def download(self, url, headers, proxies, num_retries=1, max_retries=4):

        code = 505
        try:
            r = requests.get(url, timeout=DEFAULT_TIMEOUT, headers=headers, proxies=proxies)
            code = r.status_code
            print("Downloading:", url)
            print(code)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            html = r.text

        except:
            html = None
            print("Download error:", code)
            if num_retries <= max_retries and 500 <= code <= 600:
                print("第", num_retries, "次重试:"+url)
                return self.download(url, headers, proxies, num_retries + 1)
            else:
                code = None
        return {'html': html, 'code': code}

class Throttle:
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}
    def wait(self, url):
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now()-last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
            self.domains[domain] = datetime.now()



'''def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)'''



'''
cont = '/places/default/view/Afghanistan-1/#/my/'
up = urldefrag(cont)
print(up)
regex_html = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
link = regex_html.findall(cont)
link1 = ''.join(link)
print(link1)
links = re.match('/places/default/(index|view)/(\S+)', link1)
print(links)

if __name__ == '__main__':
    link_crawl('http://example.webscraping.com', '/places/default/(index|view)/(\S+)', delay=1, num_retries=1, user_agent='BadCrawler')
    link_crawl('http://example.webscraping.com', '/places/default/(index|view)/(\S+)', delay=1, num_retries=1, max_depth=1, user_agent='GoodCrawler')'''
