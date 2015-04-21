import nltk
import re
from nltk.tag import *
from pymongo import MongoClient	
from storageTools.mongo_tools import *
from entities.statistics import *

#relationships between entities present in the same article
def entities_same_document(entitie_name):

	relationships = {}

	cursor = entities_mongo_helper() 

	for document in cursor.find():
		for name in document['entities']:
			if name in relationships.keys(): 
				doc = cursor.find({'entities' : entitie_name})
				for ar in doc:
					for entity in ar['entities']:
						if not (entity == name or entity in relationships.get(name)): # already exists relationship
							relationships[name].append(entity)
						else: continue
							

			else:
				if name == entitie_name: relationships.setdefault(name, []) 

	return relationships






				




