import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_ads")
def get_ads():
    ads = list(mongo.db.ads.find())
    return render_template("ads.html", ads=ads)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                     request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    ads = list(mongo.db.ads.find())

    if session["user"]:
        return render_template("profile.html", username=username, ads=ads)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/post_ad", methods=["GET", "POST"])
def post_ad():
    if request.method == "POST":
        is_available = "on" if request.form.get("is_available") else "off"
        ad = {
            "category_name": request.form.get("category_name"),
            "ad_title": request.form.get("ad_title"),
            "ad_description": request.form.get("ad_description"),
            "photo_url": request.form.get("photo_url"),
            "price": request.form.get("price"),
            "condition_type": request.form.get("condition_type"),
            "location": request.form.get("location"),
            "email": request.form.get("email"),
            "telephone": request.form.get("telephone"),
            "is_available": is_available,
            "posted_by": session["user"]
        }
        mongo.db.ads.insert_one(ad)
        flash("Ad Successfully posted")
        return redirect(url_for("get_ads"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    conditions = mongo.db.conditions.find().sort("condition_type", 1)
    return render_template("post_ad.html", categories=categories,
                           conditions=conditions)


@app.route("/edit_ad/<ad_id>", methods=["GET", "POST"])
def edit_ad(ad_id):
    if request.method == "POST":
        is_available = "on" if request.form.get("is_available") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "ad_title": request.form.get("ad_title"),
            "ad_description": request.form.get("ad_description"),
            "photo_url": request.form.get("photo_url"),
            "price": request.form.get("price"),
            "condition_type": request.form.get("condition_type"),
            "location": request.form.get("location"),
            "email": request.form.get("email"),
            "telephone": request.form.get("telephone"),
            "is_available": is_available,
            "posted_by": session["user"]
        }
        mongo.db.ads.update({"_id": ObjectId(ad_id)}, submit)
        flash("Ad Successfully Updated")

    ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    conditions = mongo.db.conditions.find().sort("condition_type", 1)
    return render_template("edit_ad.html", ad=ad, categories=categories,
                           conditions=conditions)


@app.route("/delete_ad/<ad_id>")
def delete_ad(ad_id):
    mongo.db.ads.remove({"_id": ObjectId(ad_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_ads"))


@app.route("/view_ad/<ad_id>")
def view_ad(ad_id):
    ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)})

    return render_template("view_ad.html", ad=ad)


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# @app.route("/profile/<username>/<ad_id>", methods=["GET", "POST"])
# def profile(username=None, ad_id=None):
#     # grab the session user's username from the db
#     username = mongo.db.users.find_one(
#         {"username": session["user"]})["username"]

#     ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)})

#     if session["user"]:
#         return render_template("profile.html", username=username, ad=ad)

#     return redirect(url_for("login"))


# @app.route("/wish/<ad_id>")
# def wish(ad_id):
#     ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)})

#     return render_template("profile.html", ad=ad)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
