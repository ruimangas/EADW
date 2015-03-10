from whoosh.index import open_dir
from whoosh.qparser import *

def query(word=sys.argv[1:]):
	a = []
	t = word[0].decode("unicode-escape")
	ix = open_dir("indexdir")

	with ix.searcher() as searcher:
		query = QueryParser("content", ix.schema, group=OrGroup).parse(t)
		results = searcher.search(query, limit=100)
		for r in results:
			a.append(int(str(r["id"])))
	return sorted(a)

print query()