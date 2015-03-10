from whoosh.index import create_in
from whoosh.fields import *

file = open("aula03_cfc.txt", 'r')

schema = Schema(id = NUMERIC(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()

for l in file:
	writer.add_document(id=int(l[:5]),content=unicode(l[5:],"utf-8"))

writer.commit()