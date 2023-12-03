from app import app
from flask import render_template

# Define routing views for Staff Portal
@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/jinja')
def jinja():

    my_name = "Mack"

    return render_template("public/jinja.html", my_name=my_name)