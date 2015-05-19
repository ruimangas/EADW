import os 

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
    features = []
    for feature in FEATURES:
        features.append(feature in words)

    return features

print get_features("house chair school blood anyone letter adult key and cococ")
            

