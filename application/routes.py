import datetime, pandas
from flask import request, render_template, make_response, url_for, redirect, flash
from datetime import datetime as dt
from flask import current_app as app
from .models import User, Exercise
from .forms import ExerciseForm
from . import db


@app.route('/home')
@app.route('/')
def home():
    """Landing page"""
    return render_template("home.html",
                           title="Homepage",
                           description="This is the home page for the strength_app!  Select a page to begin."
                           )


@app.route('/workout', methods=['GET', 'POST'])
def workout():
    """Page where you enter a workout"""
    title = "Enter Workout"
    description = "Enter new workout data here"
    form = ExerciseForm()
    df = pandas.read_sql_table("Exercise", db.engine)
    if request.method == 'POST':
        date = datetime.datetime.now()
        name = request.form['name']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']
        rest = request.form['rest']
        notes = request.form['notes']
        record = Exercise(date=date, name=name, sets=sets, reps=reps, weight=weight, rest=rest, notes=notes)
        db.session.add(record)
        db.session.commit()
        flash('New exercise successfully saved!')
        return redirect('workout')

    return render_template("workout.html",
                           title=title,
                           description=description,
                           form=form,
                           data=df
                           )


@app.route('/progress', methods=['GET', 'POST'])
def progress():
    """Page where you review workout progress"""
    return render_template("progress.html",
                           title="Workout Progress",
                           description="Review workout progress here",
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
