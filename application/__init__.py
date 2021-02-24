# TODO BACKLOG
# https://www.youtube.com/watch?v=XTpLbBJTOM4
#       save added records between app launches (currently having trouble with Exercise.id being recognized...)
#       properly track / update the id numbers
# Complete add, edit, delete modals and connect with database
# Nutrition (my fitness pal API)
# Fitbit (steps, sleep data API)
# Convert homepage have links to strength, baseline, nutrition pages
# Add table filtering
# Develop plan for backing up csv file
# use g, teardown app context when requests are over
# Add visualization functionality
# Add data validation
# Add login / authentication
# Git pull request
# Tag project history
# CLI library in python
# Turn into official package


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

    # Create exercise table from input file upon every launch
    exercise_df = pd.read_csv('input_data.csv')
    exercise_df.to_sql('Exercise', db.get_engine(app=app), if_exists='replace')

    return app
