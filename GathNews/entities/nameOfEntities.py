import nltk
import re
from nltk.tag import *
from pymongo import MongoClient	
from storageTools.mongo_tools import *


def list_of_entities(link):
	client = MongoClient('localhost', 27017)
	db = client.eadw
	news = db.news

	names_file = open("./res/output.txt", "r").readlines()
	entities = []
	for line in names_file:
		entities.append(line.strip())

	organizations_file = open("./res/output2.txt","r").readlines()
	organizations = []
	for l in organizations_file:
		organizations.append(l.strip())

	article = news.find_one({"link" : link}) #get specific doc from mongo

	allEntities = []
	print "checking..."
	for sentence in nltk.sent_tokenize(article["document"]):
		for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)), binary=False):
			if hasattr(chunk, "label"):
				if chunk.label() == "PERSON" or chunk.label() == "ORGANIZATION":
					et = " ".join(c[0] for c in chunk.leaves())
					if et in entities or et in organizations:
						if et not in allEntities:
							allEntities.append(et)

	insert_new_collections(allEntities,article)

	print "DONE!"

def insert_new_collections(allPersons, oldArticle):
	client = MongoClient('localhost', 27017)
	db = client.eadw
	peps = db.namesOfPersons

	newArticle = oldArticle
	newArticle['entities'] = allPersons
	peps.update({"link":newArticle['link']}, newArticle, True);

def retrieve_entities(link):
	client = MongoClient('localhost', 27017)
	db = client.eadw
	peps = db.namesOfPersons

	report = peps.find_one({"link" : link})

	if report['entities']:
		return report['entities']
	else: return ["No entities found."]







