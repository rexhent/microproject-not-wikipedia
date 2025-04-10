from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/register')
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