#!/usr/bin/python

import sqlite3

CREATE_NEWS_TABLE = """ CREATE TABLE IF NOT EXISTS news
                            (link TEXT PRIMARYKEY,
                             title TEXT NOT NULL,
                             date TEXT NOT NULL);"""

INSERT_FORMATTER = "INSERT INTO news VALUES (?,?,?);"


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
    def insert(self, link, title, date):
        """
            Attempts to insert the values into the database
            returns the success of the operation
        """
        try:
            with self.conn:
                self.conn.execute(INSERT_FORMATTER, (link, title, date))
            return True
        except sqlite3.IntegrityError:
            return False


    def _open_newsdb_(self):
        conn = sqlite3.connect('newsdb')
        cursor = conn.cursor()
        cursor.execute(CREATE_NEWS_TABLE)
        return (conn, cursor)
