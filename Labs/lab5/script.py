import numpy as np
from numpy import linalg

def lregression(X,y):
    l = len(y)
    A = np.vstack([np.array(X).T, np.ones(l)])
    return linalg.lstsq(A.T,y)[0]

def start(lines=open("aula05_features.txt","r").readlines()):
	X = []
	y = []
	for line in lines:
		array = line.split()
		X.append((array[0],array[1],array[2]))
		y.append(array[3])
	print lregression(X,y)

start()


