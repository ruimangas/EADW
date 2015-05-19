import os 
import nltk

def remove_stop_words():
    stop_words = []
    for filen in os.listdir('../lab6'):
        if filen.startswith('stop'):
            with open('../lab6/' + filen) as f:
                stop_words += map(lambda s:s.strip(), f.readlines())

    return stop_words

def polarity(file = open('aula10_polarity.txt','r')):
    return set(reduce(lambda a,b: a + b.split()[1:], file.readlines(), [])).difference(remove_stop_words())

FEATURES = polarity()

def get_features(input):
    words = input.split()
    features = {}
    for feature in FEATURES:
        features[feature] = feature in words

    return features

def nbc_classifier(file = open('aula10_polarity.txt','r')):
    examples = []
    for line in file:
        f_class = "positive" if line[0] == '+' else "negative"
        examples.append((get_features(line),f_class))
    
    return examples

classifier = nltk.NaiveBayesClassifier.train(nbc_classifier())
estimated_class = classifier.classify(get_features("Hot Tub Time Machine proved title when it earned fairly positive reviews and some decent money"))
print estimated_class

     
            

