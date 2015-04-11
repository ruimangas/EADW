#!/usr/bin/python

import feedparser
from threading import Thread
import os
from read_html import parseHTML
from dbstorage import NewsDatabase

NEWS_LIMIT = 99

def html_parser_thread(link, date):
    """
        Thread called for parsing html from the link and storing
        the resulting contents into the storage
    """
    news = parseHTML(link)
    if not news: return ##something wrong happened

    success = NewsDatabase().insert(link, news[0], date)
    #if success : NewsIndexing().store(news[0], ' '.join(news[1:]))



def rss_parser_thread(rss, limit=NEWS_LIMIT):
	"""
        This thread picks all the news links and
		calls another thread to parse the html for every article
		limit the max number of threads to start from the url

	"""
	d = feedparser.parse(rss)
	threads = [Thread(target=html_parser_thread, args=(entry.link, entry.published))
                for entry in d.entries ][:limit]
	for thr in threads: thr.start()
	for thr in threads: thr.join()

    #print "Finished: ", rss

def init(filepath="rss.txt"):
    """
        Parses the rss file for the rss links,
        for each url calls a thread to deals with it
	"""
    rss_filter = lambda string: not string.isspace() and string.lstrip()[0] != '#'

    with open(filepath) as f:
        lines = filter(rss_filter, f.readlines())

    threads = [Thread(target=rss_parser_thread, args=(line,)) for line in lines]
    for thr in threads: thr.start()
    for thr in threads: thr.join()

if __name__ == '__main__':
    init()
    print "<ALL DONE>"
