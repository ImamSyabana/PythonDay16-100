from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Email, Length, URL
import csv
from flask_bootstrap import Bootstrap5
from markupsafe import Markup
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

all_books = []

Bootstrap5(app)

class BookForm(FlaskForm):
    book = StringField(label = 'Book Name', validators=[DataRequired()])
    author = StringField(label = 'Book Author', validators=[DataRequired()])
    rating = StringField(label = 'Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')

@app.route('/', methods=['GET', 'POST'])
def home():
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

        all_books.append(temp_dict)
        print(all_books)
    return render_template("add.html", books = all_books, form = form)


if __name__ == "__main__":
    app.run(debug=True)

