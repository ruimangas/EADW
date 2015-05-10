import nltk
import re
from nltk.tag import *
from pymongo import MongoClient	
from storageTools.mongo_tools import *
from entities.statistics import *

#relationships between entities present in the same article
def entities_same_document(entitie_name):

    relationships = {}
    relationships.setdefault(entitie_name, [])

    cursor = entities_mongo_helper() 

    for document in cursor.find():
        for name in document['entities']:
            if name not in relationships.keys() and (name and entitie_name in document['entities']):
                relationships[entitie_name].append(name)

    return relationships	






