from cs50 import SQL
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///froshims0.db")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if request.form["name"] == "" or request.form["continent"] == "" or request.form["email"] == "" or request.form["phone"] == "":
        return render_template("failure.html")
    db.execute("INSERT INTO registrants (name, continent, email, phone) VALUES(:name, :continent, :email, :phone)",
        name = request.form["name"], continent = request.form["continent"], email = request.form["email"], phone = request.form["phone"])
    return render_template("success.html")


@app.route("/registrants")
def registrants():
    rows = db.execute("SELECT * FROM registrants")
    render_template("registrants.html", rows=rows)
