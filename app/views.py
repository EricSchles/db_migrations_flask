from app import app
from flask import render_template
from app.models import Data

@app.route("/",methods=["GET","POST"])
def index():
    d = Data.query.all()
    d_length = len(d)
    return render_template("index.html",data=d,length=d_length)
