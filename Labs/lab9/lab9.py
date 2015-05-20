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
    if 'polarity.txt' in os.listdir('.'):
        print "There is a cached word file, do you want to get a new one?[ y / n ]"
        opt = raw_input(">> ")
        if opt == 'n':
            with open('polarity.txt') as f:
                return map(lambda s:s.strip(),f.readlines())

    num_words = int(raw_input("Select number of words to be chosen\n>>"))
    words = reduce(lambda a,b: a+b.split()[1:], file.readlines(), [])
    words = list(set(words).difference(remove_stop_words()))[:num_words] #return only 2000 words (have no clue if popular)        
    with open('polarity.txt', 'w+') as f:
        for word in words:
            f.write(word + "\n")
    return words

FEATURES = polarity()
print "polarity done."
def get_features(input):
    words = input.split()
    features = {}
    for feature in FEATURES:
        features[feature] = feature in words

    return features

def nbc_classifier(file = open('aula10_polarity.txt','r')):
    examples = []
    for line in file:
        examples.append((get_features(line),line[0]))
    
    return examples


classifier = nltk.NaiveBayesClassifier.train(nbc_classifier())
estimated_class = classifier.classify(get_features("Hot Tub Time Machine proved title when it earned fairly positive reviews and some decent money"))
print "Class: [" + estimated_class + "]"

     
            

