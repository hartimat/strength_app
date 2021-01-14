from flask import request, render_template, make_response, url_for, redirect
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User


@app.route('/home')
@app.route('/')
def home():
    """Landing page"""
    return render_template("home.html",
                           title="Homepage",
                           description="This is the home page for the strength_app!  Select a page to begin."
                           )


@app.route('/log', methods=['GET', 'POST'])
def log():
    """Page where you enter a workout"""
    date = request.args.get('date')
    exercise = request.args.get('exercise')
    sets = request.args.get('sets')
    reps = request.args.get('reps')
    weight = request.args.get('weight')
    rest = request.args.get('rest')
    notes = request.args.get('notes')
    return render_template("log.html",
                           title="Workout Logging Page",
                           description="Enter a new workout, or modify an old one here."
                           )


@app.route('/users', methods=['GET'])
def users():
    """Create a user via query's string parameters"""
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        if existing_user:
            return make_response(
                "This user already exists, dummy!"
            )
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="In west philadelphia born and raised, \
                on the playground is where I spent most of my days",
            admin=False
        )   # create instance of user class
        db.session.add(new_user)    # add new user record to db
        db.session.commit()     # commit db changes
        return '<h1>Something broke for user route</h1>'
    return render_template(
        "users.html",
        users=User.query.all(),
        title="Show Users"
    )
