from flask import Flask, render_template
from post import Post
import requests

URL_blogPost = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(URL_blogPost)
all_posts= response.json()

post_list = []
for post in all_posts:
    post_objects = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_list.append(post_objects)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", postRendered = post_list)

@app.route('/<int:index>')
def get_post(index):
    return render_template("post.html", id = index, postRendered = post_list)

if __name__ == "__main__":
    app.run(debug=True)
