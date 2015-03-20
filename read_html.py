#!/usr/bin/python
import urllib
from bs4 import BeautifulSoup


def parseHTML(news_url, specificParser):
    """
        Opens an url and parses the html for important data to be stored
    """
    res = urllib.urlopen(news_url)
    if res.getcode() != 200: return
    soup = BeautifulSoup(res.read())
    res.close()
    return specificParser(soup)


def diarioNoticiasParser(soup):
    title = soup.find(id='NewsTitle').string
    text = soup.find(id='Article')
    return [title] + [s.string for s in text.find_all('p')]

def jornalNoticiasParser(soup):

    title = soup.find(id='newsTitle').string
    post_title = soup.find_all('div','postTitle')[0].string
    text = soup.find(id='Article')
    return [title, post_title] + [s.string for s in text.find_all('p')]


if __name__ == '__main__':
    parseHTML("http://feeds.jn.pt/~r/JN-ULTIMAS/~3/9iB77Axg2DQ/Interior.aspx", jornalNoticiasParser)

#O dn tem varios tipos de rss, adicionar todos
