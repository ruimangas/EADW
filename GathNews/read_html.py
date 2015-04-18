#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import re

REQUEST_TIMEOUT_SECS = 20

DN = 'dn'
JN = 'jn'
CM = 'xl'   ## domainGet only works for the xl in http://www.cmjornal.xl.pt/

def domainGet(link):
    return re.search(re.compile('.(?P<dom>\w+).pt'), link).group('dom')

def parseHTML(news_url):
    """
        Opens an url and parses the html for important data to be stored
    """
    parser = html_parsers[domainGet(news_url)]
    if not parser: return
    try:
        res = urllib2.urlopen(news_url, timeout=REQUEST_TIMEOUT_SECS)
        if not res.getcode() == 200: return

        encoding = res.headers['content-type'].split('charset=')[-1]
        ucontent = unicode(res.read(), encoding)

        soup = BeautifulSoup(ucontent.encode(encoding))
        res.close()
        return parser(soup)
    except: return



def diarioNoticiasParser(soup):
    title = soup.find(id='NewsTitle')
    text = soup.find(id='Article')

    if not title or not text: return

    try:
        return [title.string] + [s.getText() for s in text.find_all('p')]
    except:
        return None

def jornalNoticiasParser(soup):
    title = soup.find(id='newsTitle')
    post_title = soup.find_all('div','postTitle')
    text = soup.find(id='Article')

    #Parser must return title and body
    if not title or not text: return
    try:
        return [title.string] + [post_title[0].getText()]\
            + [s.string for s in text.find_all('p') if s.string ]
    except:
        return None


def correioManhaParser(soup):
    title = soup.find_all('div', 'NoticiaTituloTxt')
    post_title = soup.find_all('div', 'NoticiaTituloSubTxt')
    text = soup.find_all('div', 'mioloNoticia')

    if not title or not text: return
    try:
        return [title[0].string] + [post_title[0].getText()]\
                + [s.getText() for s in text[0].find_all('p') if s.getText() ]
    except:
        return None
"""
class DomainNotFoundError(Exception):
    def __init__(self, domain):
        self.dom = domain
    def __repr__(self):
        return self.dom + " has no parser available"
"""

html_parsers = {
    DN: diarioNoticiasParser,
    JN: jornalNoticiasParser,
    CM: correioManhaParser
}


if __name__ == '__main__':
    parseHTML("http://feeds.jn.pt/~r/JN-ULTIMAS/~3/9iB77Axg2DQ/Interior.aspx", jornalNoticiasParser)
