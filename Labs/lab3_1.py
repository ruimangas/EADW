from collections import Counter

def inverted_index(file=open("teste_file_ex1.txt","r")):
	dic={}
	my_count={}
	var=0
	for line in file.readlines():
		for w in line.split():
			try: my_count[w] += 1
			except KeyError: my_count[w] = 1
		for word in set(line.split()):
			dic.setdefault(word, []).append((var,my_count[word]))
		var+=1
		my_count.clear()
	return dic

def print_dic(dictionary):
	for (key,value) in dictionary.items():
		print key + " -> " + str(value)

print_dic(inverted_index())





