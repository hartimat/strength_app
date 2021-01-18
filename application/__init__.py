# TODO
# Enter and save exercise data in db from form on screen
# Add login / authentication
# Add CSS / JS
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

    # Populate database
    exercise_df = pd.read_csv('input_data.csv')
    exercise_df.to_sql('Exercise', db.get_engine(app=app), if_exists='replace')



    return app
