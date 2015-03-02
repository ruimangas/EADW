print(len(list(set(open('file.txt', 'r').read().split()).intersection(open('file2.txt', 'r').read().split()))))
