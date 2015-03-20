#!/usr/bin/python

import feedparser
from threading import Thread
import os
import read_html

NUM_NEWS = 10

def rss_parser_thread(rss):
    d = feedparser.parse(rss)
    threads = []
    for (count, entry) in enumerate(d.entries, start=1):
        if count > NUM_NEWS: break
        thread = Thread(target=read_html.parseHTML, args=(entry.link,read_html.jornalNoticiasParser))
        threads.append(thread)
        thread.start()
    for thr in threads:
        thread.join()
    print "Finished: ", rss


rss_filter = lambda string: not string.isspace() and string.lstrip()[0] != '#'


if __name__ == '__main__':
    with open('rss.txt') as f:
        lines = filter(rss_filter, f.readlines())
        
    threads = []
    for line in lines:
        if line.lstrip() and line.lstrip()[0] == '#': continue
        thread = Thread(target=rss_parser_thread, args=(line,))
        threads.append(thread)
        thread.start()
    for thr in threads:
        thread.join()
    print "<ALL DONE>"

