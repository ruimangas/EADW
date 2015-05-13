import nltk
import re
from nltk.tag import *
from pymongo import MongoClient	
from storageTools.mongo_tools import *
import plotly.plotly as py
from plotly.graph_objs import *

def count_entities(searchName):

	count_dic = {}

	file = open("./res/output.txt", "r").readlines()
	entities = []
	for line in file:
		entities.append(line.strip())

	cursor = entities_mongo_helper().find()

	if searchName in entities:
		for doc in cursor:
			if searchName in doc['entities']:
				for name in doc['entities']:
					if name == searchName:
						if name not in count_dic.keys():
							count_dic[name] = 1
						else: count_dic[name] += 1
    
	return count_dic

def famous_personalities():

	popularity_dic = {}

	cursor = entities_mongo_helper().find()

	for article in cursor:
		for name in article['entities']:
			if name not in popularity_dic.keys():
				popularity_dic[name] = 1
			else: popularity_dic[name] += 1

	new_list = []

	for key, value in popularity_dic.items():
		if value == max(list(popularity_dic.values())):
			new_list.append(key)

	print "The most famous entities are: " + ",".join(new_list)

	#names_e = []
	#number_e = []

	#for name_et, number in popularity_dic.items():
		#names_e.append(name_et)
		#number_e.append(number)

	#data = Data([
		#Bar(
			#x = names_e,
			#y = number_e
		#)
	#])

	#plot_url = py.plot(data, filename='basic-bar')









