from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import find_dotenv, load_dotenv
from flask import session
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-ranking.db"

Bootstrap5(app)


# membuat form untuk edit dan add
class EditForm(FlaskForm):
    edited_rating = StringField(label = '',
                                validators=[DataRequired()],
                                render_kw={'placeholder': 'New Rating'})
    edited_review= StringField(label = '',
                                validators=[DataRequired()],
                                render_kw={'placeholder': 'New Review'})
    # edited_ranking= StringField(label = '',
    #                             validators=[DataRequired()],
    #                             render_kw={'placeholder': 'New Ranking'})
    submit = SubmitField('Change Rating')

class AddForm(FlaskForm):
    add_title =StringField(label = '',
                            validators=[DataRequired()],
                            render_kw={'placeholder': 'New Title Entry'})
    submit = SubmitField('Add Movie')
# CREATE DB

# inisiasi database
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)

# CREATE TABLE
class Movies_db(db.Model):
    id_num: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True, type_=String(250))
    year : Mapped[str] = mapped_column(nullable=False, type_=String(4))
    description : Mapped[str] = mapped_column(nullable=False, type_=String(250))
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=False, type_=String(250))
    img_url: Mapped[str] = mapped_column(nullable=False)

# create table yang telah di defined
with app.app_context():
    db.create_all()

# menambahkan data pertama ke database
new_movie = Movies_db(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

second_movie = Movies_db(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)


# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movies_db).order_by(Movies_db.rating.asc()))
        #all_movies = result.scalars()
        all_movies = list(result.scalars())

        for x in range(len(all_movies)):
            rank = (len(all_movies) - x)
            all_movies[x].ranking = rank
        
    return render_template("index.html", movies = all_movies)

@app.route("/add", methods=['GET', 'POST'])
def add_records():
    form = AddForm()
    results = []
    if form.validate_on_submit():
        title = form.add_title.data

        temp_dict = {
            "title" : title
        }

        # mempersiapkan API The Movie Database (TMDB)
        # mencari lokasi file .env secara otomatis 
        dotenv_path = find_dotenv()

        # load the entries as environtment variables
        load_dotenv(dotenv_path)

        # stored the env variables within a python variable
        API_KEY= os.getenv("API_KEY_TMDB")
        API_read_access_token = os.getenv("API_read_access_token_TMDB")
        headers = os.getenv("headers_TMDB")

        
        headers_dict = {
            "accept": "application/json",
            "Authorization": f"Bearer {headers}"
        }
        
        # parameter dict
        parameters = {
            "query" : temp_dict["title"],
            "include_adult" : False,
            "language" : "en-US",
            "page" : 1
        }

        URL =  f"https://api.themoviedb.org/3/search/movie?query={parameters['query']}&include_adult={parameters['include_adult']}&language={parameters['language']}&page={parameters['page']}"

        # membuatt request ke API forecast
        response = requests.get(url = URL, headers = headers_dict)
        response.raise_for_status()

        search_result = response.json()
        print(search_result['results'])

        results = search_result['results']

        return render_template('select.html', results = results)


    return render_template('add.html', form = form)

@app.route('/<int:id>', methods= ['GET', 'POST'])
def select_results(id):
    movie_id = id
    #print(movie_id)

    # use the id to fetch all the data from Movie Database API on that movie
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = os.getenv("headers_TMDB")

    headers_dict = {
        "accept": "application/json",
        "Authorization": f"Bearer {headers}"
    }

    response = requests.get(url = url, headers=headers_dict)

    response.raise_for_status()

    search_result = response.json()
    #print(search_result)

    add_selected_movie = Movies_db(
    id_num=search_result["id"], 
    title=search_result["original_title"],
    year=search_result["release_date"][:4],
    description=search_result["overview"],
    rating=4.6,
    #ranking=8,
    review="Lorem Ipsum",
    img_url=f"https://image.tmdb.org/t/p/w500{search_result['poster_path']}"
    )


    with app.app_context():
        db.session.add(add_selected_movie)
        db.session.commit()
    
    return redirect(url_for('edit_records', id = search_result['id']))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_records(id):
    # Get the book_id from the URL query string
    movie_id = id

    # check the post available from database
    with app.app_context():
        movie_to_update = db.get_or_404(Movies_db, movie_id)

    editform = EditForm()

    if editform.validate_on_submit():
        rating = editform.edited_rating.data
        review = editform.edited_review.data
        #ranking = editform.edited_ranking.data

        temp_rating = {
            "rating": rating,
            "review": review,
            #"ranking" : ranking
        }

        # Load the book from the database
        with app.app_context():
            # movie yang mau diupdatte
            movie_to_update = db.session.execute(db.select(Movies_db).where(Movies_db.id_num == movie_id)).scalar()
            # rating dan movie pengganti
            movie_to_update.rating = temp_rating["rating"]
            movie_to_update.review = temp_rating["review"]
            #movie_to_update.ranking = temp_rating['ranking']
            db.session.commit()

        return redirect(url_for("home"))

    # Render the form for GET request
    return render_template("edit.html", movie=movie_to_update, form = editform)

@app.route('/delete', methods=['GET', 'POST'])
def delete_records():
    # Get the book_id from the URL query string
    movie_id = request.args.get('id', type=int)

    # Load the book from the database
    with app.app_context():
        # records yang mau dihapus
        movie_to_delete = db.session.execute(db.select(Movies_db).where(Movies_db.id_num == movie_id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()

    # Render the form for GET request
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)
