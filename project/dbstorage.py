#!/usr/bin/python

import sqlite3

CREATE_NEWS_TABLE = """ CREATE TABLE IF NOT EXISTS news 
                            (link TEXT PRIMARYKEY,
                             title TEXT NOT NULL,
                             body TEXT NOT NULL,
                             date TEXT NOT NULL);"""
INSERT_FORMATTER = u""" INSERT INTO news VALUES
                        ('{}','{}','{}','{}');"""


def customInsert(formatter, cursor):
    def insert(*args, **kwargs):
        print args
        cursor.execute(formatter.format(*args))
        if (kwargs['commit']): cursor.commit()
    return insert

def open_newsdb(): 
    conn = sqlite3.connect('newsdb')
    cursor = conn.cursor()
    cursor.execute(CREATE_NEWS_TABLE)
    return (conn, cursor)


