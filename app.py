from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hi. I'm Adejola Ogunsan</p>"

@app.route("/projects")
def show_projects():
    return "<p>showing projects</p>"

@app.route("/photography")
def show_photography():
    return "<p>showing photography</p>"

@app.route("/github") #<- add the link here
def github():
    return "<p>taking you to github!</p>"