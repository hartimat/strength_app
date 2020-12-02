from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from werkzeug.utils import secure_filename
app = Flask(__name__)

# TODO
# Create rough pages, nav bar
# Add css, js (bootstrap?)
# Build each page one-by-one
# Link db
# Features: db, link to myfitnesspal, cookies, sessions, authenticate, web/mobile, wtforms, form check vids


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/create_template')
def create_template():
    return render_template('create_template.html')


@app.route('/create_workout')
def create_workout():
    return render_template('create_workout.html')


@app.route('/edit_workout')
def edit_workout():
    return render_template('edit_workout.html')


@app.route('/display_data')
def display_data():
    return render_template('display_data.html')


# index
# create_template
# create_workout
# edit_workout
# display_data


if __name__ == '__main__':
    app.secret_key = 'SECRET KEY'
    app.run(debug=True)
