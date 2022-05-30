from flask import Flask
from flask import request,redirect,url_for
from flask import render_template
from flask import session
import time
import threading

app = Flask(__name__, static_folder="static", static_url_path="/")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    place=request.form['Stadium']
    time=request.form['Time']
    print(place,time)
    return render_template("index.html", result="Result: ", score="?????????")
    
@app.route("/subscribe", methods=['POST'])
def subscribe():
    return render_template("index.html", result="Result: ", score="?????????")
    
if __name__ == "__main__":
    app.run(port=5000)
