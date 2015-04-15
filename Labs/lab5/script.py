import numpy as np
from numpy import linalg
from whoosh import scoring
from whoosh.index import open_dir
from whoosh.qparser import *
import pageRank

def lregression(X,y):
    l = len(y)
    A = np.vstack([np.array(X).T, np.ones(l)])
    return linalg.lstsq(A.T,y)[0]

def start(lines=open("aula05_features.txt","r").readlines()):
	X = []
	y = []
	for line in lines:
		array = line.split()
		X.append((array[0],array[1], array[2]))
		y.append(array[3])
	return lregression(X,y)


def whooshOpen(query):
	ix = open_dir("../lab3/indexdir")

	results_dict = {}

	query = QueryParser('content', ix.schema).parse(query)
	with ix.searcher(weighting=scoring.TF_IDF()) as s_tf:
		tf_results = s_tf.search(query, limit=100)
    	for r in tf_results:
    		results_dict.setdefault(r.docnum, []).append(r.score)


	with ix.searcher(weighting=scoring.BM25F()) as s_bm:
		bm_results = s_bm.search(query, limit=100)
		for r in bm_results:
			results_dict.setdefault(r.docnum, []).append(r.score)


	ranks = pageRank.pageRank(pageRank.inverted_index, 0.85, 10)

	
	l = []
	for (id, vals) in results_dict.iteritems():
		if len(vals) == 2:
			l.append((vals[0], vals[1], ranks[id]))

	expected = start()

			
	ys = []
	for (tf, bm, pr) in l:
		ys.append(bm*expected[0] + tf*expected[1] + pr*expected[2]+ expected[3])

	print ys

if __name__ == '__main__':
	#start()
	whooshOpen(raw_input(">>"))


