#!/usr/bin/python
import os
import sys
import feedparser
from threading import Thread
from read_html import parseHTML
from storageTools.whoosh_tools import NewsIndexing
from storageTools.mongo_tools import *
from entities.nameOfEntities import *

NEWS_LIMIT = 99

def html_parser_thread(link, date):
    """
        Thread called for parsing html from the link and storing
        the resulting contents into the storage
    """
    news = parseHTML(link)
    if not news: return

    success = addNews(link, news[0], date,  ' '.join(news[1:]))
    indexing.insert(link, news[0], ' '.join(news[1:]))
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


def index_news(filepath="res/rss.txt"):
    rss_filter = lambda string: not string.isspace() and string.lstrip()[0] != '#'
    with open(filepath) as f:
        lines = filter(rss_filter, f.readlines())

    threads = [Thread(target=rss_parser_thread, args=(line,)) for line in lines]
    for thr in threads: thr.start()
    for thr in threads: thr.join()
    print "<ALL DONE>"


def search(query):
    return indexing.search(query)

def search_news():
    query = raw_input("Please enter something to search for: ")
    results = search(query)
    print str(len(results)) + " Articles found:"
    show_results(results)

def show_results(results):
    for r in results:
        print getNews(r)

def show_all_news():
    for n in getAllnews():
        print n['title'] + ":\n" + n['document'] + "\n"
    news = list_of_entities()
    print "FOUND " + str(len(news)) + " PERSON NAMES."
    for name in news:
        print name

def init():
    """
        Parses the rss file for the rss links,
        for each url calls a thread to deals with it
	"""
    cmd_line()


def cmd_line():
    options = {
        '1': lambda:index_news(),
        '2': lambda:search_news(),
        '3': lambda:show_all_news(),
        '0': lambda:sys.exit(0)
    }
    with open("res/titlescreen.txt") as f:
        print f.read()

    while 1:
    	print "1) Fetch News"
    	print "2) Search news"
        print "3) Get All News"
        print "0) Quit"

        cmd = raw_input(">>").strip()
        if options.has_key(cmd): options[cmd]()
        else:
            print "Invalid Command"

global indexing
indexing = NewsIndexing()

if __name__ == '__main__':
    init()
