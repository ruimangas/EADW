def inverted_index(file=open("teste_file_ex1.txt","r")):
	dic={}
	var=0
	for i in file.readlines():
		for a in set(i.split()):
			dic.setdefault(a, []).append(var)
		var+=1

	return dic

def print_dic(dictionary):
	for (key,value) in dictionary.items():
		print key + " -> " + str(value)

print_dic(inverted_index())


