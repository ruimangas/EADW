import sys
import re
dic={}
def inverted_index(file=open("lab02_documents.txt","r")):
	line_spliter = re.compile('\W+')
	my_count={}
	var=1
	for line in file.readlines():
		for w in line_spliter.split(line):
			try: my_count[w] += 1
			except KeyError: my_count[w] = 1
		for word in set(line_spliter.split(line)):
			dic.setdefault(word, []).append((var,my_count[word]))
		var+=1
		my_count.clear()
	return dic

def print_dic(dictionary):
	for (key,value) in dictionary.items():
		print key + " -> " + str(value)

def document_frequency(words=sys.argv[1:]):
	maxi = 0
	print "****************"
	for k in words:
		print k + " -> " + str(len(dic[k]))	
		for i in dic[k]:
			if i[1] > maxi:
				maxi = i[1]
		print "maximo: " + str(maxi)
		maxi=0
	print "****************"

print_dic(inverted_index())
document_frequency()
print str(len(open("lab02_documents.txt","r").readlines())) + " documents"
print str(len(dic.keys())) + " terms"








