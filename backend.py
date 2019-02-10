import sqlite3

class Database:
    def __init__(self, fname):
        self.fname = fname
        self.conn = sqlite3.connect(self.fname)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def add_entry(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        
    def delete(self, id):
        self.cur.execute("DELETE FROM bookstore WHERE id=?",(id, ))
        self.conn.commit()
        
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()
        
    def view_all(self):
        self.cur.execute("SELECT * FROM bookstore")
        rows = self.cur.fetchall()
        return rows

    def search(self, title='', author='', year='', isbn='', strict=False):
        if strict:
            self.cur.execute("SELECT * FROM bookstore WHERE title=? AND author=? AND year=? AND isbn=?", (title, author, year, isbn))
        else:
            self.cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

if __name__ == "__main__":
    print('backend --> Database class definition')
