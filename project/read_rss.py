#!/usr/bin/python

import feedparser
from threading import Thread
import os
from read_html import parseHTML
import dbstorage

NEWS_LIMIT = 1;

def html_parser_thread(link, date):
    """
        Thread called for parsing html from the link and storing 
        the resulting contents into the storage
    """
    news = parseHTML(link)
    if not news: return ##something wrong happened
    (cursor, conn) = dbstorage.open_newsdb()
    insert = dbstorage.customInsert(dbstorage.INSERT_FORMATTER, cursor)
    insert(link, news[0], ' '.join(news[1:]), date, commit=True)
    conn.close()


def rss_parser_thread(rss):
    d = feedparser.parse(rss)
    threads = [Thread(target=html_parser_thread, args=(entry.link, entry.published))
                for entry in d.entries ][:NEWS_LIMIT]
    for thr in threads: 
        thr.start()
    for thr in threads:
        thr.join()
    print "Finished: ", rss


rss_filter = lambda string: not string.isspace() and string.lstrip()[0] != '#'


if __name__ == '__main__':

 
    with open('rss.txt') as f:
        lines = filter(rss_filter, f.readlines())

    threads = [Thread(target=rss_parser_thread, args=(line,)) for line in lines]
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()

    print "<ALL DONE>"

