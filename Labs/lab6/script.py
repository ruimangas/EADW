from __future__ import division
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

import re
import os

def blacklist((word, setcount)):
	perc = len(setcount) / len(train.data)
	return (len(setcount) >= 3 and perc < 0.9) if word.isalpha() else False
		

stop_words = []
for filen in os.listdir('.'):
	if filen.startswith('stop'):
		with open(filen) as f:
			stop_words += map(lambda s:s.strip(), f.readlines())

train = fetch_20newsgroups(subset='train')
test = fetch_20newsgroups(subset='test')

if 'files' not in os.listdir('.'):
	os.mkdir('files')

appears = {}
stop_regex = '|'.join(stop_words)


for i,data in enumerate(train.data):
	data =re.sub(r'\b{}\b'.format('('+stop_regex+')'), '', data) #not the best solution, will also remove  substr of words (meal != me) -> al
	train.data[i] = data.split(':')[-1]		#again not the best way, supposes no : is used on the text
	
	if 'banned.txt' not in os.listdir('.'):
		for word in data.split():
			appears.setdefault(word, set()).add(i)

if 'banned.txt' not in os.listdir('.'):
	banned = map(lambda x :x[0], filter(blacklist, appears.items()))
	banned_regex = '|'.join(banned).encode('utf-8')

	with open('banned.txt', 'w') as f:
		f.write(banned_regex)
else:
	banned_regex = open('banned.txt').read()

print "Doing last check"
for i,data in enumerate(train.data):
	train.data[i] = re.sub(r'\b{}\b'.format('('+banned_regex+')'), '', data)
	with open('files/'+str(i)+".txt", 'w') as f:
		f.write(train.data[i].encode('utf-8')) 


vectorizer = TfidfVectorizer()
trainvec = vectorizer.fit_transform(train.data)
testvec = vectorizer.transform(test.data)
classifier = MultinomialNB()
classifier.fit(trainvec, train.target)
classes = classifier.predict(testvec)

print metrics.accuracy_score(test.target, classes)
print metrics.precision_score(test.target, classes)
# etc.
print metrics.classification_report(test.target, classes)
