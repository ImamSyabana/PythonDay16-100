from flask import Flask, render_template
import requests

app = Flask(__name__)

URL ="https://api.npoint.io/d0920cd6fc5224231f0e"
response = requests.get(URL)
response_data = response.json()

#print(response_data[0])
@app.route('/')
def home_page():
    return render_template("index.html", all_posts = response_data)


@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/<int:idx>')
def post_page(idx):
    return render_template('post.html', postContent = response_data[idx -1 ])


if __name__ == "__main__":
    app.run(debug=True)
