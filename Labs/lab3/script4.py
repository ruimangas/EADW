from __future__ import division
from whoosh.index import open_dir
from whoosh.qparser import *
import math

FILENAME = "aula03_queries.txt"
FOLDER_NAME = "indexdir"

file = open(FILENAME,'r').readlines()
ix = open_dir(FOLDER_NAME)
query_results = []
query_goal = []

avg_intersection = 0
avg_precision = 0 
avg_recall = 0

for i in range(len(file))[::2]:
	a = []
	with ix.searcher() as searcher:
		query = QueryParser("content", ix.schema, group=OrGroup).parse(file[i])
		results = searcher.search(query, limit=100)
		for r in results:
			a.append(int(str(r["id"])))
	query_results.append(a)

for i in range(len(file))[1::2]:
	query_goal.append(map(int,file[i].split()))

for (retrived,relevant) in zip(query_results,query_goal):
	intersect = len(list(set(retrived).intersection(relevant)))
	precision = float(intersect)/len(set(retrived))
	recall = float(intersect)/len(set(relevant))
	if (precision == 0.0) | (recall == 0.0):
		f1 = 0.0
	else: f1 = 2*((precision*recall)/(precision+recall))
	print "p " + str(precision)
	print "r " + str(recall)
	print "f " + str(f1)

	avg_intersection += intersect / 100
	avg_precision += precision / 100
	avg_recall += recall / 100

print "AVERAGEVALUES:"
print avg_intersection
print avg_precision 
print avg_recall