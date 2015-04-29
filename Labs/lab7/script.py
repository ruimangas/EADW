from urllib2 import urlopen

import os
import re
import md5
import time
import urlparse
import robotparser

FOLDER = "webhtml"

def full_url(endpoint):
	reg = 'http:\/\/|https:\/\/'
	return urlparse.urljoin(domain, endpoint) if not re.match(reg, endpoint) else endpoint


def robot_file(domain):
	rp = robotparser.RobotFileParser(urlparse.urljoin(domain, "robots.txt"))
	rp.read()
	def _clos(url):
		return rp.can_fetch("*", url)
	return _clos


def filter_links (urls):
	urls = filter(lambda l: not l.startswith("#"),urls)
	return set(filter(lambda l:l.startswith("http://") and is_accessible(l), map(full_url,urls)))


def has_topic(html, topics):
	ratio = 2/3
	topics_re = "{}".format("|".join(topics))
	print re.findall(topics_re, html, re.I)
	return len(re.findall(topics_re, html, re.I)) > ratio * len(topics)

def open_links(urls, depth=1, done_links = [] , topic=[]):

	linksre = '<a\s.*?href=[\'"](.*?)[\'"].*?</a>'

	if not depth:
		print "Depth Exceeded, bye."
		return done_links

	for url in urls:
		if url in done_links: continue
		print "Parsing:", url
		done_links.append(url)

		html = urlopen(url).read()
		if topic and not has_topic(html, topic): continue
		with open(FOLDER + "/" + md5.new(url).hexdigest(),'w+') as f: f.write(html)
		
		ls = filter_links(re.findall(linksre, html, re.I))
		time.sleep(1)
	return open_links(ls, depth - 1, done_links, topic=topic)



if __name__ == '__main__':
	global domain
	global is_accessible
	p2p = ["p2p", "peer", "kademlia", "dht", "pastry", "chord"]

	with open('urls.txt') as f:
		lines = f.readlines()
	if FOLDER not in os.listdir('.'):
		os.mkdir(FOLDER)

	for line in lines:
		domain = line.strip()
		is_accessible = robot_file(domain)	
		ls = open_links([domain], depth=2, topic = p2p)



