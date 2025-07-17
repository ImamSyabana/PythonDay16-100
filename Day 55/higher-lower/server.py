from flask import Flask
import random

#mendefinisikan angka yang perlu ditebak
secretNumber = random.randint(0,9)
print(secretNumber)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>' 

@app.route('/<int:gueseNum>')
def guessed_result(gueseNum):
    if gueseNum == secretNumber:
        return '<h1 style = "color : green">You found me!</h1>' \
            '<img src = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnM4MGk0YmswN2NqbjlqNTdlcTZycGVsYmhyY2o1Y3ZrdWw3cDM3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26tknCqiJrBQG6bxC/giphy.gif"/>'
    elif gueseNum < secretNumber:
        return '<h1 style = "color : red">Too low, try again!</h1>' \
            '<img src = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHVtcDdxZmxodnpieWF6M28zeDJ5NXM0ZWZvaGtlYmNoNXF4eXlqYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/13rQ7rrTrvZXlm/giphy.gif"/>'
    elif gueseNum > secretNumber:
        return '<h1 style = "color : purple">Too high, try again!</h1>' \
            '<img src = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHVtcDdxZmxodnpieWF6M28zeDJ5NXM0ZWZvaGtlYmNoNXF4eXlqYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/toXKzaJP3WIgM/giphy.gif"/>'


        
# Run the app if this file is excecuted
if __name__ == '__main__':
    app.run(debug=True)
    


