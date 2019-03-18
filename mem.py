# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:31:53 2019

@author: BRQ
"""

import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()

def cria():
    cur.execute("create table people (name_last, age)")
    who = "Yeltsin"
    age = 72
    # This is the qmark style:
    cur.execute("insert into people values (?, ?)", (who, age))
    return

def ler():
    # And this is the named style:
    cur.execute("select * from people where name_last=:who and age=:age", {"who": who, "age": age})
    print (cur.fetchone())
    return

cria()
ler()

