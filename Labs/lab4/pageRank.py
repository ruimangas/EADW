from __future__ import division

# d -> dumping factor
# l -> interactions
# graph -> dictionary

lines = open("aula04_links.txt").readline()
inverted_index = {}

for line in lines:
	a = map(int, line.strip().split())
	for link in a[1:]:
		inverted_index.setdefault(link, set()).add(a[0])

def pageRank(graph,d,l):
	number = len(graph)
	dic = {}
	pageRank = {key: 1/len(graph) for key in graph.keys()}
	pageRank_next = pageRank.copy()
	for (key,value) in graph.iteritems():
		dic[key] = len(value)
	for i in range(l):
		for (j, val) in graph.iteritems():
			pageRank_next[j] = d*(1/number)+(1-d)*sum([pageRank[link]/dic[link] for link in val])
		pageRank = pageRank_next.copy()
	return pageRank

print pageRank({1:[3],2:[1,3],3:[1,2]},0.1,2)












