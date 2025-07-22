from flask import Flask

app = Flask(__name__)

def emphasis_decorator(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def bold_decorator(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def underlined_decorator(function):
    def wraper():
        return f"<u>{function()}</u>"
    return wraper

@app.route('/')
def hello_world():
    return "<h1>Hello World! </h1>"

@app.route('/bye')
@emphasis_decorator
@underlined_decorator
@bold_decorator
def goodbye():
    return "bye!"



# Run the app if this file is excecuted
if __name__ == '__main__':
    app.run(debug=True)
    
    
