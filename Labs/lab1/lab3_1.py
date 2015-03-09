import re
dic={}
def inverted_index(file=open("teste_file_ex1.txt","r")):
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

print_dic(inverted_index())
print str(len(open("teste_file_ex1.txt","r").readlines())) + " documents"
print str(len(dic.keys())) + " terms"


