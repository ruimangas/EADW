import nltk
import re
from nltk.tag import *
from pymongo import MongoClient	


def list_of_entities():
	client = MongoClient('localhost', 27017)
	db = client.test
	news = db.news

	file = open("output.txt", "r").readlines()
	entities = []
	for line in file:
		entities.append(line.strip())

	cursor = news.find() #get all news
	allThePeople = []
	for article in cursor:
		print "checking " + article["title"]
		for sentence in nltk.sent_tokenize(article["document"]):
			for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))):
				if hasattr(chunk, "label"):
					if chunk.label() == "PERSON":
						people = " ".join(c[0] for c in chunk.leaves())
						if people in entities:
							if people not in allThePeople:
								allThePeople.append(people)
						else: continue

	print "DONE!"
	return allThePeople
	