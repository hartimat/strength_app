import pandas
import json
from flask import request, render_template, make_response, url_for, redirect, flash, g
from sqlalchemy import MetaData, Table
from datetime import datetime as dt
from flask import current_app as app
from .models import User, Exercise
from .forms import ExerciseForm
from . import db


@app.route('/home')
@app.route('/')
def home():
    """Landing page"""
    title = "Homepage"
    df = pandas.read_sql_table("Exercise", db.engine)
    form = ExerciseForm()

    return render_template("home.html",
                           title=title,
                           columns=df.columns,
                           rows=df.iterrows(),
                           form=form
                           )


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        id = Exercise.query.order_by(Exercise.id.desc())
        id = id.first() + 1
        date = request.form['date']
        name = request.form['name']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']
        rest = request.form['rest']
        notes = request.form['notes']
        record = Exercise(id=id, date=date, name=name, sets=sets, reps=reps, weight=weight, rest=rest, notes=notes)

        db.session.add(record)
        db.session.commit()

        flash("New Exercise Successfully Added")

        return redirect(url_for('home'))


@app.route('/workout', methods=['GET', 'POST'])
def workout():
    """Page where you enter a workout"""
    title = "Workout Log"
    form = ExerciseForm()
    df = pandas.read_sql_table("Exercise", db.engine)
    if request.method == 'POST':
        jsonData = request.get_json()
        updated_exercise = Exercise(int(float(jsonData['index'])), str(jsonData['date']), str(jsonData['name']), int(jsonData['sets']), str(jsonData['reps']), float(jsonData['weight']), float(jsonData['rest']), str(jsonData['notes']))
        db.session.add(updated_exercise)
        db.session.commit()
        # query the table for the record whose index matches
        # update the values in the record based on ajax data
        # commit / save the changes to the db table
        # return to the workout webpage (check that changed data persists on reload)
        # FIXME: handle form submission vs table submission
        # date = datetime.datetime.now()
        # name = request.form['name']
        # sets = request.form['sets']
        # reps = request.form['reps']
        # weight = request.form['weight']
        # rest = request.form['rest']
        # notes = request.form['notes']
        # record = Exercise(date=date, name=name, sets=sets, reps=reps, weight=weight, rest=rest, notes=notes)
        # db.session.add(record)
        # db.session.commit()

        return redirect(url_for('workout'))

    return render_template("workout.html",
                           title=title,
                           description=description,
                           form=form,
                           columns=df.columns,
                           rows=df.iterrows()
                           )


@app.route('/progress', methods=['GET', 'POST'])
def progress():
    """Page where you review workout progress"""
    print('were in the progress route')
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
