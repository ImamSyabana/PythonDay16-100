from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# inisiasi database
class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# initialize the app with the extension
db.init_app(app)

# define table named books yang akan dibuat
class Books(db.Model):
    id_num: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True, type_=String(250))
    author: Mapped[str] = mapped_column(nullable=False, type_=String(250))
    rating: Mapped[float] = mapped_column(nullable=False)

# create table yang telah di defined
# with app.app_context():
#     db.create_all()

book_record = Books(
             title= "Harry Potter",
             author= "J. K. Rowling",
             rating = 9.3)

# menambahkan data ke datatbase
# with app.app_context():
#     db.session.add(book_record)
#     db.session.commit()

# Read All Records
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()

print(all_books)


# Read A Particular Record By Query
with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()

print(book)


# Update A Particular Record By Query
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harrysss Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit() 

# Update A Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.id_num == book_id)).scalar()
    # or book_to_update = db.get_or_404(Books, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()  

# Delete A Particular Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.id_num == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()