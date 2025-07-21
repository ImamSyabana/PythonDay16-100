from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/538a50d879cec785affc"
response = requests.get(blog_url)
all_posts = response.json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template("index.html", kumpulan_posts = all_posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
    
    
if __name__ == "__main__":
    app.run(debug=True)
