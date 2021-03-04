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
                           form=form,
                           dataframe=df
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


@app.route('/update/<row_id>', methods=['POST'])
def update(row_id):
    if request.method == 'POST':
        record = Exercise.query.get(int(row_id))

        record.date = request.form['date']
        record.name = request.form['name']
        record.sets = request.form['sets']
        record.reps = request.form['reps']
        record.weight = request.form['weight']
        record.rest = request.form['rest']
        record.notes = request.form['notes']

        db.session.add(record)
        db.session.commit()

        flash('Exercise Successfully Updated')
    return redirect(url_for('home'))
