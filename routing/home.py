from flask import Blueprint, render_template

app = Blueprint('home', __name__)

@app.route('/')
def halamanUtama():
    return render_template("home.html")