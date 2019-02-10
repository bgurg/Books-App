import sqlite3

fname = 'books.db'

def init_table():
    conn = sqlite3.connect(fname)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT)")
    conn.commit()
    conn.close()

def add_entry(title, author, year, isbn):
    conn = sqlite3.connect(fname)
    cur = conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect(fname)
    cur = conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE id=?",(id, ))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect(fname)
    cur = conn.cursor()
    cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

def view_all():
    conn = sqlite3.connect(fname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title='', author='', year='', isbn='', strict=False):
    conn = sqlite3.connect(fname)
    cur = conn.cursor()
    if strict:
        cur.execute("SELECT * FROM bookstore WHERE title=? AND author=? AND year=? AND isbn=?", (title, author, year, isbn))
    else:
        cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    print('backend module')
else:
    init_table()
