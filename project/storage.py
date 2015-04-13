#!/usr/bin/python

import sqlite3
import os.path
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.writing import AsyncWriter
from whoosh.index import open_dir
from whoosh.qparser import *

CREATE_NEWS_TABLE = """ CREATE TABLE IF NOT EXISTS news
                            (link TEXT PRIMARY KEY,
                             title TEXT NOT NULL,
                             date TEXT NOT NULL,
                             document TEXT NOT NULL);"""

INSERT_FORMATTER = "INSERT INTO news VALUES (?,?,?,?);"


class NewsDatabase:

    def __init__(self):
        (self.conn, self.cursor) = self._open_newsdb_()

    def commit_and_close(dbfunc):
        def _dec_(self, *args):
            success = dbfunc(self,*args)
            self.conn.commit()
            self.conn.close()
            return success
        return _dec_

    @commit_and_close
    def insert(self, link, title, date, document):
        """
            Attempts to insert the values into the database
            returns the success of the operation
        """
        try:
            with self.conn:
                self.conn.execute(INSERT_FORMATTER, (link, title, date, document))
            return True
        except sqlite3.IntegrityError:
            return False


    def _open_newsdb_(self):
        conn = sqlite3.connect('newsdb')
        cursor = conn.cursor()
        cursor.execute(CREATE_NEWS_TABLE)
        return (conn, cursor)

class NewsIndexing:

    def __init__(self):
        self.TARGET_DIR = "NewsIndex"
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
