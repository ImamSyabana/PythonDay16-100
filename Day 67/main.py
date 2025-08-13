from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# INITIALIZE CKEditor
ckeditor = CKEditor(app)

# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# create new post form
class PostForm(FlaskForm):
    title = StringField(label = 'Blog Post Title', validators=[DataRequired()])
    subtitle = StringField(label = 'Blog Post Subtitle', validators=[DataRequired()])
    author = StringField(label = 'Your name', validators=[DataRequired()])
    img_url = StringField(label = 'Blog Image URL', validators=[DataRequired()])
    body = CKEditorField(label = 'Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit POST')

@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []

    with app.app_context():
        result = db.session.execute(db.select(BlogPost))
        posts = list(result.scalars())
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post =    "Grab the post from your database"

    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    #all_posts = result.scalars().all()

    selected_post = {
        "id": requested_post.id,
        "title":requested_post.title,
        "date":requested_post.date,
        "body":requested_post.body,
        "author":requested_post.author,
        "img_url":requested_post.img_url,
        "subtitle":requested_post.subtitle,
    }

    return render_template("post.html", post=selected_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods = ["GET","POST"])
def add_new_post():
    form = PostForm()

    if form.validate_on_submit():
        # yang merecord di kolom form
        title = form.title.data
        subtitle = form.subtitle.data
        author = form.author.data
        img_url = form.img_url.data
        body = form.body.data
        

        # dictionary yang menyimpan nilai di kolom sementara 
        temp_dict = {
            "title" : title,
            "subtitle" : subtitle,
            "author" : author,
            "img_url" : img_url,
            "body" : body
            
        }

        # menyiapkan records object untuk dimasukkan ke database
        new_post_record = BlogPost(
            title = temp_dict["title"],
            subtitle = temp_dict["subtitle"],
            author = temp_dict["author"],
            img_url = temp_dict["img_url"],
            body = temp_dict["body"],
            date = (date.today()).strftime("%B %d, %Y")
        )

        # menambahkan data ke datatbase.
        with app.app_context():
            db.session.add(new_post_record)
            db.session.commit()
        
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form = form, is_edit = False)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods = ["GET","POST"])
def edit_post(post_id):
    postID= post_id

    # check the post available from database
    post_to_update =db.get_or_404(BlogPost, postID)

    editform = PostForm(
        title=post_to_update.title,
        subtitle=post_to_update.subtitle,
        img_url=post_to_update.img_url,
        author=post_to_update.author,
        body=post_to_update.body
    )

    if editform.validate_on_submit():
        # yang merecord di kolom form
        title = editform.title.data
        subtitle = editform.subtitle.data
        author = editform.author.data
        img_url = editform.img_url.data
        body = editform.body.data

        edit_temp_dict = {
            "title" : title,
            "subtitle" : subtitle,
            "author" : author,
            "img_url" : img_url,
            "body" : body
        }

        # load the original post from the database
        with app.app_context():
            # post yang diupdatte 
            post_to_update = db.session.execute(db.select(BlogPost).where(BlogPost.id == postID)).scalar()
            # value pengganti
            post_to_update.title = edit_temp_dict["title"]
            post_to_update.subtitle = edit_temp_dict["subtitle"]
            post_to_update.author = edit_temp_dict["author"]
            post_to_update.img_url = edit_temp_dict["img_url"]
            post_to_update.body = edit_temp_dict["body"]

            db.session.commit()

        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form = editform, is_edit = True)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>', methods = ["GET","POST"])
def delete_post(post_id):
    postID= post_id

    # Load the book from the database
    with app.app_context():
        # records yang mau dihapus
        post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == postID)).scalar()
        db.session.delete(post_to_delete)
        db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
