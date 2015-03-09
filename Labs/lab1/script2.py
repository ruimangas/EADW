file = open('file.txt', 'r')
lines = file.read()
my_count = {}
for word in lines.split():
	try: my_count[word] += 1
	except KeyError: my_count[word] = 1
for (key,value) in my_count.items():
	print key + ":" + str(value)
