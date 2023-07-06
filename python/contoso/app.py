from flask import Flask, redirect, url_for, request, render_template, session
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/user/dangerous/<username>')
def show_user_profile_dangerous(username):
    return f'User {(username)}'
