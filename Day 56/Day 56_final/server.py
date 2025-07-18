from flask import Flask
import random
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")
        
# Run the app if this file is excecuted
if __name__ == '__main__':
    app.run(debug=True)
    


