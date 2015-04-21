import nltk
import re
from nltk.tag import *
from pymongo import MongoClient	
from storageTools.mongo_tools import *

def count_entities(searchName):

	count_dic = {}

	client = MongoClient('localhost', 27017)
	db = client.eadw
	peps = db.namesOfPersons

	file = open("./res/output.txt", "r").readlines()
	entities = []
	for line in file:
		entities.append(line.strip())

	cursor = peps.find()

	if searchName in entities:
		for doc in cursor:
			if searchName in doc['entities']:
				for name in doc['entities']:
					if name == searchName:
						if name not in count_dic.keys():
							count_dic[name] = 1
						else: count_dic[name] += 1


	else: return "Invalid Name"

	return count_dic






