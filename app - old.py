from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.column(db.String(100))
    complete =db.Column(db.Boolen)


 


@app.route('/')
def home():
    return 'Hello God please do something with my Life'


@app.route('/base')
def home1():
    return render_template("base.html")


if __name__ == "__main__":
    app.run()
