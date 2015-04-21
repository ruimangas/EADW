import nltk
import re
from nltk.tag import *
from pymongo import MongoClient	
from storageTools.mongo_tools import *


def list_of_entities(link):
	client = MongoClient('localhost', 27017)
	db = client.eadw
	news = db.news

	file = open("./res/output.txt", "r").readlines()
	entities = []
	for line in file:
		entities.append(line.strip())

	article = news.find_one({"link" : link}) #get specific doc from mongo

	allThePeople = []
	print "checking..."
	for sentence in nltk.sent_tokenize(article["document"]):
		for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)), binary=False):
			if hasattr(chunk, "label"):
				if chunk.label() == "PERSON":
					people = " ".join(c[0] for c in chunk.leaves())
					if people in entities:
						if people not in allThePeople:
							allThePeople.append(people)

	insert_new_collections(allThePeople,article)

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


	












