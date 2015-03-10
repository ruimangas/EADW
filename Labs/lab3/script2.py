from whoosh.index import open_dir
from whoosh.qparser import *

ix = open_dir("indexdir")

with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema, group=OrGroup).parse(u"first method")
    results = searcher.search(query, limit=100)
    for r in results:
        print r
    print "Number of results:", results.scored_length()