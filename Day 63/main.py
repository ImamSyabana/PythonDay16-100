from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Email, Length, URL
import csv
from flask_bootstrap import Bootstrap5
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
# inisiasi database
class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection-final.db"

# initialize the app with the extension
db.init_app(app)

all_books = []

Bootstrap5(app)

# form untuk entry
class BookForm(FlaskForm):
    book = StringField(label = 'Book Name', validators=[DataRequired()])
    author = StringField(label = 'Book Author', validators=[DataRequired()])
    rating = StringField(label = 'Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')

# form untuk editt rating
class EditForm(FlaskForm):
    edited_rating = StringField(label = '',
                                validators=[DataRequired()],
                                render_kw={'placeholder': 'New Rating'})
    
# MEMBUAT DATABASE
# define table named books yang akan dibuat
class Books_db(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    book_title: Mapped[str] = mapped_column(nullable=False, unique=True, type_=String(250))
    author: Mapped[str] = mapped_column(nullable=False, type_=String(250))
    rating: Mapped[float] = mapped_column(nullable=False)

# create table yang telah di defined
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    with app.app_context():
        result = db.session.execute(db.select(Books_db).order_by(Books_db.book_title))
        #all_books = result.scalars()
        all_books = list(result.scalars())
    return render_template("index.html", books = all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    
    if form.validate_on_submit():
        book = form.book.data
        author = form.author.data
        rating = form.rating.data

        temp_dict = {
            "title" : book,
            "author": author,
            "rating": rating
        }

       

        book_record = Books_db(
             book_title= temp_dict["title"],
             author= temp_dict["author"],
             rating = temp_dict["rating"])

        # menambahkan data ke datatbase.
        with app.app_context():
            db.session.add(book_record)
            db.session.commit()

    return render_template("add.html", form = form)

@app.route('/edit', methods=['GET', 'POST'])
def edit_rating():
    # Get the book_id from the URL query string
    book_id = request.args.get('id', type=int)

    # Load the book from the database
    with app.app_context():
        book_to_update = db.get_or_404(Books_db, book_id)

    editform = EditForm()
    
    if editform.validate_on_submit():
        rating = editform.edited_rating.data
        
        temp_rating = {
            "rating": rating
        }
        
        edit_record =Books_db(
             rating = temp_rating["rating"])
        
    # # Handle the POST request (form submission)
    # if request.method == 'POST':
    #     new_rating = request.form.get('rating')
    #     with app.app_context():
    #         book_to_update.rating = float(new_rating)
    #         db.session.commit()
    #     return redirect(url_for('home'))

    # Render the form for GET request
    return render_template("edit.html", book=book_to_update, form = editform)


if __name__ == "__main__":
    app.run(debug=True)

