import sqlite3
import os.path
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.writing import AsyncWriter
from whoosh.index import open_dir
from whoosh.qparser import *

class NewsIndexing:

    def __init__(self):
        self.TARGET_DIR = "newsIndex"
        if not os.path.exists(self.TARGET_DIR):
            os.mkdir(self.TARGET_DIR)
            self.schema = Schema(link=TEXT(stored=True),\
                                 title=TEXT,\
                                 document=TEXT)
            self.ix = create_in(self.TARGET_DIR, self.schema)
        else:
            self.ix = open_dir(self.TARGET_DIR)

    def insert(self, link, title, document):
        writer = AsyncWriter(self.ix)
        writer.add_document(link=link,title=title, document=document + title)
        writer.commit()


    def search(self,content):
        a = []
        with self.ix.searcher() as searcher:
            query = QueryParser("document", self.ix.schema, group=OrGroup).parse(content.decode())
            results = searcher.search(query, limit=100)
            for r in results:
                a.append(r["link"])
        return a