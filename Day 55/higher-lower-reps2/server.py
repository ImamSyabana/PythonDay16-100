from flask import Flask
import random

random_number = random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"

@app.route('/<int:number>')
def guessed_number(number):
    if number == random_number:
        return "<h1 style = 'color:green'>You are correct </h1>" \
            "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"
    elif number < random_number:
        return "<h1 style = 'color:red'>Too low, try again!</h1>" \
            "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
    
    elif number > random_number:
        return "<h1 style = 'color:purple'>Too high</h1>" \
            "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
    
# Run the app if this file is excecuted
if __name__ == '__main__':
    app.run(debug=True)