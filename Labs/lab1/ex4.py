print(len(set(open('lab02_documents.txt', 'r').read().lower().split()).intersection(open('teste_file_ex1.txt', 'r').read().lower().split())))
