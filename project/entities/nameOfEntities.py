import nltk
import re
from nltk.tag import *
import pymongo


def list_of_entities():
	file = open("personalidades.txt", "r").readlines()
	entities = {}
	for line in file:
		print line
		entities = line
	print entities
