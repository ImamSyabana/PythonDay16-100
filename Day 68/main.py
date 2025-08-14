from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, get_flashed_messages
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
# conect database dengan app
db.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

# create a registration form
class RegistForm(FlaskForm):
    email = StringField(label = "Email", validators = [DataRequired()])
    name = StringField(label = "Name", validators = [DataRequired()])
    password = PasswordField(label = "Password", validators = [DataRequired()])
    submit = SubmitField('Submit POST')



# initiate login manager object
login_manager = LoginManager()
# conect login manager dengan app
login_manager.init_app(app)

#Set the login view: Flask-Login will redirect unauthenticated users to this route.
login_manager.login_view = "login"



# Assuming you have a User model (nama databasenya User). It must inherit from UserMixin.
# class User(UserMixin, db.Model):
#     ...

@login_manager.user_loader
def load_user(id):
    if id:
        return db.get_or_404(User, int(id))
    return None



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    
    if request.method == "POST":
        # mengambil yang ada di kolom input HTML
        name = request.form['name']
        email = request.form["email"]

        # convert password menjadi hash + salt
        password = request.form['password']
        password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        
        user_to_register = db.session.execute(db.select(User).where(User.email == email)).scalar()
        
        # kalo email sudah exist maka user_to_register ada isinya 
        # berarti ngga boleh register
        if user_to_register:
            # Handle existed credentials
            flash('You have signed up with that email, log in instead.', 'error')
            return redirect(url_for('login'))
        
        # kalo email belum exist berarti user_to_register return None
        # berarti email belum pernah dipake dan boleh register.
        elif not(user_to_register):
            # menyiapkan records object USER untuk dimasukkan ke database
            new_user = User(
                email = email,
                password = password,
                name = name
            )

            # menambahkan data ke datatbase.
            db.session.add(new_user)
            db.session.commit()
            
            # login the new user
            login_user(new_user)

            return render_template("secrets.html", name = name)
    
    return render_template("register.html")


@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        # mengambil yang ada di kolom input HTML
        email = request.form["email"]
        password = request.form['password']

        user_to_login = db.session.execute(db.select(User).where(User.email == email)).scalar()
        

        # Login and validate the user.
        # user should be an instance of your `User` class
        # Check if the user exists and the password is correct
        if not(user_to_login):
            # Handle invalid credentials
            flash('Invalid email. Please try again.', 'error')
            return redirect(url_for('login'))
        elif check_password_hash(user_to_login.password, password) == False:
            # Handle invalid credentials
            flash('Invalid password. Please try again.', 'error')
            return redirect(url_for('login'))
        else:
            #flash('You were successfully logged in!', 'success')
            login_user(user_to_login)
            return render_template("secrets.html", name = user_to_login.name)
        
            
        
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="D:/_Coolyeah/Udemy/100Days Python/Day 68/static/files",   # Folder where the file is stored
        path="cheat_sheet.pdf",       # The file name to serve
        as_attachment=True   # Forces browser to download instead of open in tab
    )

if __name__ == "__main__":
    app.run(debug=True)
