from flask import Flask
from flask import render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    now = datetime.now()
    formatted_date = now.strftime("%Y")
    randomNumber = random.randint(1,10)
    return render_template("index.html", num = randomNumber, yearnow = formatted_date)

@app.route("/blog/<int:num>")
def get_blog(num):
    blog_url ="https://api.npoint.io/cf3d5cd239e9042df621"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts = all_posts)


@app.route('/blog/<string:input_name>')
def AGEnNamePredictor(input_name):
    gender_parameters = {
        "name" : input_name
    }
    response_genderAPI = requests.get("https://api.genderize.io?", params=gender_parameters)
    
    predicted_gender_data = response_genderAPI.json()
    predicted_gender = predicted_gender_data["gender"]

    age_parameters = {
        "name" : input_name
    }
    response_ageAPI = requests.get("https://api.agify.io?", params = age_parameters)
    
    predicted_age_data = response_ageAPI.json()
    predicted_age = predicted_age_data["age"]
    
    return render_template("guess.html", predGender = predicted_gender, predAge = predicted_age, userName = input_name)

if __name__ == "__main__":
    app.run(debug=True)
