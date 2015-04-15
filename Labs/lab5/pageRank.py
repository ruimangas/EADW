from __future__ import division

# d -> dumping factor
# l -> interactions
# graph -> dictionary

with open("../lab4/aula04_links.txt") as f: lines = f.readlines()
inverted_index = {}

for line in lines:
	links = map(int, line.strip().split())
	inverted_index.setdefault(links[0], set()) 
	for link in links[1:]:
		inverted_index.setdefault(link, set()).add(links[0])

def links_inverter(links_index):
	"""
		Transform a group of outbound links into inbound or inbound to outbound
	"""
	inverted_index = {}
	for (linkkey, linkset) in links_index.iteritems():
		inverted_index.setdefault(linkkey, set())   
		for link in linkset:
			inverted_index.setdefault(link, set()).add(linkkey)
	return inverted_index


def pageRank(graph, d, l):
	numNodes = len(graph) 
	pageRank = {key: 1/numNodes for key in graph.keys()}
	pageRank_next = {}

	outbound_links = {key: len(value) for (key,value) in links_inverter(graph).iteritems()}
	for i in range(l):
		for (node, inlinks) in graph.iteritems():
			pageRank_next[node] = d/numNodes +(1-d)*\
					sum([pageRank[link]/outbound_links[link] for link in inlinks])
		pageRank = pageRank_next.copy()
	return pageRank




"""
pageRank_next[j] = d*(1/numNodes)
	pageRank_next[j] += (1-d)*sum([pageRank[link]/outbound_links[link] for link in val])

	pageRank_next[node] = (1-d)/numNodes + d *\
					sum([pageRank[link]/outbound_links[link] for link in inlinks])
"""

def converge(diff=0.000001):
	"""
		Calculates iteration necessary for algorith to converge,
		d = 0.85
		(Only checks if the first item converged)
	"""
	pagerank_val, iterations = 1, 1
	while True:
		after = pageRank(inverted_index, 0.85, iterations).values()[0]
		if abs(pagerank_val - after) < diff: break
		iterations +=1
		pagerank_val = after
	print "Converged to", diff, "in",iterations,"iterations."

#converge()
#pageRank(inverted_index, 0.85,1)


# sum(pageRank(inverted_index, 0.85,10).values())








