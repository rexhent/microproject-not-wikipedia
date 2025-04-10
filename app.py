from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

class AccessLevel(Enum):
    USER = 1
    EDITOR = 2
    ADMIN = 3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    permission = db.Column(db.Enum(AccessLevel), nullable=False)


@app.route('/')
def home():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

@app.route('/view', methods=['POST'])
def view():
    content_id = request.form.get('content_id')
    content = Content.query.get(content_id)
    return render_template('view.html', content=content)

@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    return render_template('register.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/delete')
def create():
    return render_template('delete.html')

@app.route('/edit')
def create():
    return render_template('edit.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)