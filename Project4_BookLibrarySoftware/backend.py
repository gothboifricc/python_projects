import sqlite3

def connect():
    conn=sqlite3.connect("Data/MyLibrary.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT,author TEXT, year INTEGER, page INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,page):
    conn=sqlite3.connect("Data/MyLibrary.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,page))
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("Data/MyLibrary.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("Data/MyLibrary.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,page):
    conn=sqlite3.connect("Data/MyLibrary.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, page=? WHERE id=?",(title,author,year,page,id))
    conn.commit()
    conn.close()

def search(title="",author="",year="",page=""):
    conn=sqlite3.connect("Data/MyLibrary.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR page=?",(title,author,year,page))
    rows=cur.fetchall()
    conn.close()
    return rows

#update(3,"Goosebumps series","R.L. Stein",2005,9999)
#connect()
#insert("Mathematics","RD Sharma",2010,9999)
#delete(6)
#print(view())
#print(search("Secret Seven series"))
