import sqlite3

con = sqlite3.connect('almacen.db')

cur = con.cursor()

cur.execute('''CREATE TABLE urls
               (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT , leido DEFAULT 0)''')

cur.execute('''CREATE TABLE emails
               (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE)''')

con.close()