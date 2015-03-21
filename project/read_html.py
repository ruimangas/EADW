#!/usr/bin/python
import urllib
from bs4 import BeautifulSoup
import re

DN = 'dn'
JN = 'jn'



def domainGet(link):
    return re.search(re.compile('.(?P<dom>\w+).pt'), link).group('dom')

def parseHTML(news_url):
    """
        Opens an url and parses the html for important data to be stored
    """
    parser = html_parsers[domainGet(news_url)]
    if not parser: 
        raise DomainNotFoundError(news_url)
    try:
        res = urllib.urlopen(news_url)
        if not res.getcode() == 200: return
        soup = BeautifulSoup(res.read())
        res.close()
        return parser(soup)
    except IOError: return



def diarioNoticiasParser(soup):
    title = soup.find(id='NewsTitle').string
    text = soup.find(id='Article')
    return [title] + [s.string for s in text.find_all('p')]

def jornalNoticiasParser(soup):
    """
        NOTE: The page organization is not always the same,
        had 1 exception throws where newsTitle was not found (calling .string on NoneType)
    """
    title = soup.find(id='newsTitle').string
    post_title = soup.find_all('div','postTitle')[0].string
    text = soup.find(id='Article')
    return [title, post_title] + [s.string for s in text.find_all('p') if s.string ] # one of the parts may return none


class DomainNotFoundError(Exception):
    def __init__(self, domain):
        self.dom = domain
    def __repr__(self):
        return self.dom + " has no parser available"

html_parsers = {
    DN: diarioNoticiasParser,
    JN: jornalNoticiasParser
}


if __name__ == '__main__':
    parseHTML("http://feeds.jn.pt/~r/JN-ULTIMAS/~3/9iB77Axg2DQ/Interior.aspx", jornalNoticiasParser)
