from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
import random


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record
@app.route("/all", methods = ["GET", "POST"])
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafe = result.scalars().all()

    response_list = []
    for x in range(len(all_cafe)):
        response_obj = {
            "id": all_cafe[x].id,
            "name": all_cafe[x].name,
            "map_url": all_cafe[x].map_url,
            "img_url": all_cafe[x].img_url,
            "location": all_cafe[x].location,
            "seats": all_cafe[x].seats,
            "has_toilet": all_cafe[x].has_toilet,
            "has_wifi": all_cafe[x].has_wifi,
            "has_sockets": all_cafe[x].has_sockets,
            "can_take_calls": all_cafe[x].can_take_calls,
            "coffee_price": all_cafe[x].coffee_price
        }
        response_list.append(response_obj)

    return jsonify(cafe_all=response_list)

@app.route("/random", methods = ["GET", "POST"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)

    response_obj = {
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
        }
    
    return jsonify(cafe=response_obj)

@app.route("/search", methods= ["GET", "POST"])
def search_cafe():
    # Get the value of the 'loc' query parameter from the URL
    query_location = request.args.get("loc")

    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    selected_cafe = result.scalars().all()

    response_list = []
    for x in range(len(selected_cafe)):
        response_obj = {
            "id": selected_cafe[x].id,
            "name": selected_cafe[x].name,
            "map_url": selected_cafe[x].map_url,
            "img_url": selected_cafe[x].img_url,
            "location": selected_cafe[x].location,
            "seats": selected_cafe[x].seats,
            "has_toilet": selected_cafe[x].has_toilet,
            "has_wifi": selected_cafe[x].has_wifi,
            "has_sockets": selected_cafe[x].has_sockets,
            "can_take_calls": selected_cafe[x].can_take_calls,
            "coffee_price": selected_cafe[x].coffee_price
        }
        response_list.append(response_obj)
        print(response_list)
    
    if selected_cafe:
        return jsonify(cafe_all=response_list)
    else:
        # Return an error message and a 404 status code if no cafe is found
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404




# HTTP POST - Create Record
@app.route("/add", methods = ["GET", "POST"])
def add_cafes():
    try:
        # Create a new Cafe object from the data sent in the POST request
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            has_sockets=bool(request.form.get("has_sockets")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            coffee_price=request.form.get("coffee_price"),
        )

        # Add the new cafe to the database
        db.session.add(new_cafe)
        db.session.commit()

        # Return a success message
        return jsonify(response={"success": "Successfully added the new cafe."})

    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify(error={"Failed": str(e)}), 500


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
