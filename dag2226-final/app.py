# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/index.html")
def index():
    return render_template("index.html")
@app.route("/page1.html")
def page1():
    return render_template("page1.html")
@app.route("/page2.html")
def page2():
    return render_template("page2.html")

#start the server
if __name__ == "__main__":
    app.run()