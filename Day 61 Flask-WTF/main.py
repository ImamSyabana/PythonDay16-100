from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, Length

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

class MyForm(FlaskForm):
    email = StringField(label ='Email', validators=[InputRequired(message="Invalid email address."), Email("Invalid email address")])
    password = PasswordField(label ='Password', validators=[DataRequired(), Length(min=8, message="Field must be at least 8 characters long.")])
    submit = SubmitField(label = "Log In")

app.secret_key = "qwerty123"
#app.config['SECRET_KEY'] = 'qwerty123'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_WTF = MyForm()
    form_WTF.validate_on_submit()
    if form_WTF.validate_on_submit():
        email = form_WTF.email.data
        password = form_WTF.password.data
    return render_template('login.html', form = form_WTF)

if __name__ == '__main__':
    app.run(debug=True)
