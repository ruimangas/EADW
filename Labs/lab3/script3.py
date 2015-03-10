import math

def analysis(result,goal):

	#precision: fraction of retrieved documents that are relevant
	#recall: fraction of relevants documents that are received
	
	#Suppose a program for recognizing dogs in scenes from a video identifies 7 dogs in a scene containing 
	#9 dogs and some cats. If 4 of the identifications are correct, but 3 are actually cats, the program's 
	#precision is 4/7 while its recall is 4/9

	intersect = len(list(set(result).intersection(goal)))
	precision = float(intersect)/len(set(result))
	recall = float(intersect)/len(set(goal))

	if (precision == 0.0) | (recall == 0.0):
		f1 = 0.0
	else: f1 = 2*((precision*recall)/(precision+recall))

	print "correct value: " + str(intersect)
	print "precision: " + str(precision)
	print "recall: " + str(recall)
	print "f1: " + str(f1)


analysis([1,2,3,4],[1,44,22,3])

