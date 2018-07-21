#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import csv
import re
from lxml import etree
from link_crawler import link_crawl
from mongo_cache import Mongocache

class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('countries.csv', 'w'))
        self.fields = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        if re.search('/places/default/view/', url):
            tree = etree.HTML(html)
            row = []
            i = 1
            for field in self.fields:
                row.append((tree.xpath('//td[@class="w2p_fw"]'))[i].text)
                i += 1

            self.writer.writerow(row)


if __name__ == '__main__':
    link_crawl('http://example.webscraping.com/', '/places/default/(index|view)/(\S+)', delay=1, max_retries=1, max_depth=6, scrape_callback=ScrapeCallback(), cache=Mongocache())
