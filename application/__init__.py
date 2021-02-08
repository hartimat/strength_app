# TODO
# Make table entries editable (https://codewithmark.com/easily-edit-html-table-rows-or-cells-with-jquery)
# Add table filtering
# Add css to table
# Add new entries to table (through form, or table line?)
# Develop plan for backing up csv file
# Add validation of form data
# use g, teardown app context when requests are over
# Build out nutrition web pages (mfp api)
# Add login / authentication
# Add stylesheets
# Git pull request
# Tag project history
# CLI library in python


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import pandas as pd


# Globally accessible libraries
db = SQLAlchemy()
r = FlaskRedis()


def init_app():
    """Initialize the core application"""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.ProdConfig')     # production config
    app.config.from_object('config.DevConfig')     # development config

    # Initialize plugins
    db.init_app(app)
    r.init_app(app)

    with app.app_context():
        from . import routes    # import routes
        db.create_all()     # create sql tables for data models

    # Populate database from input file upon every launch
    exercise_df = pd.read_csv('input_data.csv')
    exercise_df.to_sql('Exercise', db.get_engine(app=app), if_exists='replace')

    return app
