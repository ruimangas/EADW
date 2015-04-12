#!/usr/bin/python
import os
import sys
import feedparser

from threading import Thread
from read_html import parseHTML
from storage import NewsDatabase, NewsIndexing

NEWS_LIMIT = 99

def html_parser_thread(link, date):
    """
        Thread called for parsing html from the link and storing
        the resulting contents into the storage
    """
    news = parseHTML(link)
    if not news: return ##something wrong happened

    success = NewsDatabase().insert(link, news[0], date)
    if success :
        indexing.insert(news[0], ' '.join(news[1:]))
        print "Stored: "+ news[0]



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


def index_news(filepath="rss.txt"):
    rss_filter = lambda string: not string.isspace() and string.lstrip()[0] != '#'
    with open(filepath) as f:
        lines = filter(rss_filter, f.readlines())

    threads = [Thread(target=rss_parser_thread, args=(line,)) for line in lines]
    for thr in threads: thr.start()
    for thr in threads: thr.join()
    print "<ALL DONE>"

def init():
    """
        Parses the rss file for the rss links,
        for each url calls a thread to deals with it
	"""
    global indexing
    indexing = NewsIndexing()

    cmd_line()


def cmd_line():
    options = {
        '1': lambda:index_news(),
        '0' : lambda:sys.exit(0)
    }
    with open("titlescreen.txt") as f:
        print f.read()

    while 1:

        print "1) Fetch News"
        print "0) Quit"

        cmd = raw_input(">>").strip()
        if options.has_key(cmd): options[cmd]()
        else:
            print "Invalid Command"

if __name__ == '__main__':
    init()
