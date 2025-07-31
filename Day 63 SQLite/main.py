import sqlite3

#define database
db = sqlite3.connect("books-collection.db")

#membuat cursor untuk mengedit database
cursor = db.cursor()

# membuat database
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

#insert data ke database
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()