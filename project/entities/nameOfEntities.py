import nltk
import re
from nltk.tag import *
import pymongo


def list_of_entities():
	file = open("output.txt", "r").readlines()
	entities = []
	for line in file:
		entities.append(line)
	