#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import csv
from zipfile import ZipFile
from mongo_cache import Mongocache

class AlexaCallback:
    def __init__(self, max_urls=10000):
        self.max_urls = max_urls
        self.seed_url = 'http://example.webscraping.com/'

    def __call__(self, url, html):
        urls = []
        if url == self.seed_url:
            cache = Mongocache()
            with ZipFile('top.zip') as zf:
                csv_filename = zf.namelist()[0]
                with zf.open(csv_filename, 'r') as fin:
                    lines = (line.decode('ascii') for line in fin)
                    for _, website in csv.reader(lines):
                        if 'http://' + website not in cache:
                            urls.append('http://' + website)
                            if len(urls) == self.max_urls:
                                break

        return urls