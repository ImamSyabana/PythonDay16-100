from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/{‌{url_for('login_info')}}", methods = ["POST", "GET"])
def login_info():
    pengguna = request.form['username']
    katakunci = request.form['password']
    #return render_template("login.html", user = pengguna, password = katakunci)
    return f"<h1>Name:{pengguna},Password:{katakunci}</h1>"

if __name__ == "__main__":
    app.run(debug=True)