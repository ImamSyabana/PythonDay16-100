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

@app.route('/<string:inputtedName>')
def AGEnNAMEpredictor(inputtedName):
    name = inputtedName.title()
    
    #age API
    age_API = "74da5b7156418439cde658354c6d686d"
    ageAPI_parameters = {
        "name" : f"{inputtedName}"
        #"apikey" : age_API
    }
    
    response_age_api = requests.get("https://api.agify.io?", params=ageAPI_parameters)
    response_age_api.raise_for_status()
    agedata = response_age_api.json()
    predicted_age = agedata["age"]
    
    #gender API
    genderAPI_parameters = {
        "name" : f"{inputtedName}"
    }
    
    response_gender_api = requests.get("https://api.genderize.io?", params=genderAPI_parameters)
    response_gender_api.raise_for_status()
    genderdata = response_gender_api.json()
    predicted_gener = genderdata["gender"]
    
    return render_template("API_Predictor.html", userName = name, predAge = predicted_age, predGender = predicted_gener)

    
if __name__ == "__main__":
    app.run()
