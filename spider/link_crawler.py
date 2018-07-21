#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'


import re
from urllib.parse import urljoin, urlparse, urldefrag
import urllib.robotparser
import queue
from downloader import Downloader
from mongo_cache import Mongocache
from alexa_cb import AlexaCallback

def link_crawl(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, user_agent='Aurora-Twinkle', proxies=None, max_retries=1, scrape_callback=None, cache=None):
    a_cb = AlexaCallback()

    crawl_queue = a_cb(seed_url,'as')
    seen = {seed_url: 0}
    num_urls = 0
    '''rp = get_robots(seed_url)'''
    D = Downloader(delay=delay, user_agent=user_agent, proxies=proxies, max_retries=max_retries, cache=cache)
    while crawl_queue:
        url = crawl_queue.pop()
        '''depth = seen[url]'''
        depth = -100
        '''if rp.can_fetch(user_agent, url):'''
        html = D(url)
        links = []
        if html is not None:
            if scrape_callback:
                links.extend(scrape_callback(url, html) or [])
            if depth != max_depth:
                if link_regex:
                    links.extend(link for link in get_links(html) if re.match(link_regex, link))

                for link in links:
                    link = format_link(seed_url, link)
                    if link not in seen:
                        seen[link] = depth + 1
                        if same_domain(seed_url, link):
                            crawl_queue.append(link)

            num_urls += 1
            if num_urls == max_urls:
                break
        '''else:
            print('user_agent: "'+user_agent+'" Blocked by robots.txt:', url)'''
def get_links(html):
    regex_html = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return regex_html.findall(html)

def get_robots(url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(url, '/robots.txt'))
    rp.read()
    return rp

def same_domain(url1, url2):
    return urlparse(url1).netloc == urlparse(url2).netloc

def format_link(seed_url, link):
    link, _ = urldefrag(link)
    return urljoin(seed_url, link)

if __name__ == '__main__':
    link_crawl('http://example.webscraping.com', '/places/default/(index|view)/(\S+)', delay=1, max_retries=1, user_agent='BadCrawler')
    link_crawl('http://example.webscraping.com', '/places/default/(index|view)/(\S+)', delay=1, max_retries=1, max_depth=1, user_agent='GoodCrawler')
