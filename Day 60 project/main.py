from flask import Flask, render_template, request
import requests
import smtplib
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods = ["GET","POST"])
def contact():
    if request.method == 'POST':
        receive_data()
        return render_template("contact.html", metode_req= request.method)
    else:
        return render_template("contact.html", metode_req= request.method)
    
    #return render_template("contact.html")

@app.route("/form-entry", methods = ["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    my_email = "expensivebonlap@gmail.com"
    my_password = "otlcxftlknqbeype"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() #TLS : transport layer security
        connection.login(user = my_email, password = my_password)
        connection.sendmail(from_addr = my_email, 
                            to_addrs="imamsyabana046@gmail.com", 
                            msg=f"Subject:New Message\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}")


    #return f"<h1>Successfully sent your message </h1>"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
