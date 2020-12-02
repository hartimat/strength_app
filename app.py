from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash, g
import sqlite3, os
app = Flask(__name__)

# TODO
# Link sqlite db
# Populate with basic exercises using create_exercise page
# Build create_template and/or create_workout
# Add css, js (bootstrap?)
# Features: db, link to myfitnesspal, cookies, sessions, authenticate, web/mobile, wtforms, form check vids


@app.route('/index')
def index():
    # TODO
    # Different navbar... list of buttons in middle of page
    return render_template('index.html')


@app.route('/create_exercise')
def create_exercise():
    # TODO
    # Create form that has all exercise class options available for fill-in
    # Dropdown: strength / endurance / mobility / other
    return render_template('create_exercise.html')


@app.route('/create_template')
def create_template():
    # TODO
    # Display list of exercises
    return render_template('create_template.html')


@app.route('/create_workout')
def create_workout():
    # TODO
    # Create form that has name/date fields, and list of exercises to choose from
    # Generate excel template for filling out
    # Read in excel template for mass populating data
    # Add program tag / metadata for further sorting later
    # Add individual workout
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
