from flask import Flask, render_template
import requests
from post import Post

URL = "https://api.npoint.io/c790b4d5cab58020d391"

response = requests.get(URL)
response_data = response.json()
post_list = []
for post in response_data:
    all_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_list.append(all_post)

#print(post_list[0].id)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", post = post_list)

@app.route('/<int:id>')
def get_post(id):
    return render_template("post.html",id = id, post = post_list)

if __name__ == "__main__":
    app.run(debug=True)
