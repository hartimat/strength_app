from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from werkzeug.utils import secure_filename
app = Flask(__name__)

# TODO
# Create pages
# Features: Connected to db, nutrition calculator link, cookies, sessions, authenticate, web/mobile, wtforms, upload form checks
# Research app layouts (e.g. views in one file, db in another), setup framework with blank files
# Create and link all base views (blueprint...?)
# Link CSS, js from web


@app.route('/')
def index():
    return render_template('index.html')


# index
# create_template
# create_workout
# edit_workout
# display_data


if __name__ == '__main__':
    app.secret_key = 'SECRET KEY'
    app.run(debug=True)
