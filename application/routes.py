import pandas
from flask import request, render_template, make_response, url_for, redirect, flash
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
        record = Exercise(id=Exercise.query.order_by(Exercise.id.desc()).first().id + 1,
                          date=request.form['date'],
                          name=request.form['name'],
                          sets=request.form['sets'],
                          reps=request.form['reps'],
                          weight=request.form['weight'],
                          rest=request.form['rest'],
                          notes=request.form['notes'])
        db.session.add(record)
        db.session.commit()
        flash('New Exercise Successfully Added')
        return redirect(url_for('home'))


@app.route('/delete/<row_id>', methods=['GET'])
def delete(row_id):
    if request.method == 'GET':
        row_id = str(int(row_id) + 1)
        record = Exercise.query.get(row_id)
        db.session.delete(record)
        db.session.commit()
        flash('Exercise Successfully Deleted')
        return redirect(url_for('home'))


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
