
# d -> dumping factor
# l -> interactions
# graph -> dictionary

def pageRank(graph,d,l):
	number = len(graph)
	dic = {}
	pageRank = {key: 1/len(graph) for key in graph.keys()}
	for (key,value) in graph.items():
		dic[key] = len(value)
	for i in range(1,l):
		for (j, val) in graph.iteritems():
			pageRank[j] = d*1/number+(1-d)+sum([pageRank[link]/dic[link] for link in val])
	return pageRank

print pageRank({1:[2,3],2:[1,3],3:[1,2]},0.1,3)








