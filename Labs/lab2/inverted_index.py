#!/usr/bin/python
from __future__ import print_function

import argparse
import string
import math
import sys
import re


if raw_input: input = raw_input


class TextIndexer(object):
	def __init__(self):
		self._words_dict = {}
		self._number_documents_parsed = 0

	def _parse_file(self, filename):
		"""
			Returns all documents in a file as a list in lower case
			Eliminates all punctuation
		"""
		punctuation_regex = "[" + string.punctuation + "]"
		with open(filename) as f:
			data = f.readlines()
		return [re.sub(punctuation_regex, '', document).strip().lower() for document in data]


	def dotProductForTerms(self, terms_array):
		s = dict()
		for term in terms_array:
			inverted_list = self._words_dict[term] if self._words_dict.has_key(term) else dict()
			idf = self.inverseDocumentFrequency(term)
			for (doc, term_frequency) in inverted_list.iteritems():
				if s.has_key(doc):	#if the doc is still not stored
					s[doc] += term_frequency * self.inverseDocumentFrequency(term)
				else:
					s[doc] = term_frequency * self.inverseDocumentFrequency(term)
		return s


	def parse(self, filename):
		"""
		Opens  a file, reads all words in file and
		returns a dictionary that maps the words
		to the id of the document and the and the number of times found.

		"""
		document_list = self._parse_file(filename)
		for (index, document) in enumerate(document_list, start=1):
			for word in document.split():
				if self._words_dict.has_key(word):
					if self._words_dict[word].has_key(index):
						self._words_dict[word][index] += 1
					else:
						self._words_dict[word][index] = 1
				else:
					self._words_dict[word] = {index: 1}

		self._number_documents_parsed = index

	def termDocumentFrequency(self, term):
		if self._words_dict.has_key(term):
			return len(self._words_dict[term])
		else: raise TermNotFoundError(term)

	def maxTermOccurrences(self, term):
		if self._words_dict.has_key(term):
			return max(self._words_dict[term].values())
		else: raise TermNotFoundError(term)

	def minTermOccurrences(self, term):
		if self._words_dict.has_key(term):
			return  min(self._words_dict[term].values())
		else: raise TermNotFoundException(term)

	def inverseDocumentFrequency(self, term):
		# uses integer division, words used a lot will return 0 may compromise results
		return math.log( self._number_documents_parsed / self.termDocumentFrequency(term), 2) # log of base 10 or e?

	def getWordsDictionary(self):
		return self._words_dict

	def getParsedDocumentsCount(self):
		return self._number_documents_parsed

	def getUniqueWordCount(self):
		return len(self._words_dict)

	def getTotalWordCount(self):
		return sum([word_count for word in self._words_dict.itervalues() for word_count in word.itervalues()])

class TermNotFoundError(Exception):
	def __init__(self, val):
		self.val = val
	def __str__(self):
		return repr(self.val)

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('filename',  type=str, help='the name of the file to parse')
	parser.add_argument('--terms', '-t', type=str, nargs="+" ,help='document frequency')
	args = parser.parse_args()


	textIndex = TextIndexer()
	textIndex.parse(args.filename)

	print(textIndex.getTotalWordCount())
	print(textIndex.getUniqueWordCount())

	if not args.terms: sys.exit(0)

	if args.terms > 1:
		print("DOT PRODUCT:")
		print(textIndex.dotProductForTerms(args.terms))
		print()

	for term in args.terms:
		print("{0} - document frequency: {1}".format(term, textIndex.termDocumentFrequency(term)))
		print("{0} - maximum occurrences: {1}".format(term, textIndex.maxTermOccurrences(term)))
		print("{0} - minimum occurrences: {1}".format(term, textIndex.minTermOccurrences(term)))
		print("{0} - inverse document frequency: {1}".format(term, textIndex.inverseDocumentFrequency(term)))
		print()
	#for each term print in how many documents does it appear
	#for each term print the max and min frequency
	#IDF = log(numberOfDocuments / Document frequency)
