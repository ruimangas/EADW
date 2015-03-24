#!/usr/bin/python

import os.path
from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import *
import pageRank



ranks = pageRank.pageRank(pageRank.inverted_index, 0.85, 10)


ix = open_dir("../lab3/indexdir")
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema, group=OrGroup).parse(u"first document")
    results = searcher.search(query, limit=100)

    arr = [(r['id'], ranks[r['id']]*results.score(i)) \
                    for (i,r) in enumerate(results) if r['id'] in ranks.keys()]
    final = sorted(arr, key=lambda (_, val): val, reverse=True)

    for r in final:
        print ">", r
