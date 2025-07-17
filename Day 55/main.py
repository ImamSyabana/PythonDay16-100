from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style = "text-align:center">Hello World!</h1>' \
            '<p>this is a paragraph</p>' \
            '<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBKWM14zOL7cEZoass_eu20GGIC_JEpdUHXw&s" />'

def make_bold(function):
    def wrapper_function():

        return f'<b>{function()}</b>'
    return wrapper_function
    
def make_emphasis(function):
    def wrapper_function():

        return f'<em>{function()}</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
     
        return f'<u>{function()}</u>'
    return wrapper_function
    
    
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def goodbye():
    return "good bye"

@app.route("/username/login/<name>")
def greet(name):
    return f"hello {name}!"

#membuat path dengan menambahkan path disetelah <name>
@app.route("/username/login/<name>/data")
def user_data(name):
    return f"{name} is 20 years old."


#membuat path yang di dalamnya ada /
@app.route("/username/login/<path:name>/data")
def path_convert(name):
    return f"{name} is 20 years old."


# membuat path yang variabelnya lebih dari 1
@app.route("/username/login/<name>/<int:number>")
def user_age(name,number):
    return f"Hello there {name}, you are {number} years old!"



# Run the app if this file is excecuted
if __name__ == '__main__':
    app.run(debug=True)# membuat debug mode menjadi ON