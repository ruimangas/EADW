import nltk
import re
from nltk.tag import *

def name_entities_ex1():
    s = "isto e um teste pbraz pedro rui"

    x = nltk.word_tokenize(s)
    y = nltk.pos_tag(x)
    z = nltk.ne_chunk(y, binary=True)

    print y
    print z
    
def name_entities_ex2():
    file = open("aula03_cfc.txt", "r").readlines()

    for line in file:
        sentences = nltk.sent_tokenize(line)
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        for k in nltk.chunk.ne_chunk(tagged, binary= True).subtrees():
            if k.label() == "NE":
                tree_string = str(k).encode('utf-8')
                print tree_string.split()[1].split("/")[0]

name_entities_ex1()
name_entities_ex2()
