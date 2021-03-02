# TODO BACKLOG
# https://www.youtube.com/watch?v=XTpLbBJTOM4
# Complete edit exercise
# Nutrition table (my fitness pal API)
# Fitbit table(steps, sleep data API)
# Navigation bar
# Add table filtering
# Backup scheme for db file... github? export csv?
# use g, teardown app context when requests are over
# Add visualization functionality
# Add data validation
# Add login / authentication
# Git pull request
# Tag project history
# CLI library in python
# Turn into official package
# Add unit / system testing package


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from pathlib2 import Path
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

    # Create exercise table from input file if no db exists

    try:
        db_file = Path('/application/site.db')
        if db_file.exists():
            pass
    except:
        print("Creating db from input csv file")
        exercise_df = pd.read_csv('input_data.csv')
        exercise_df.to_sql('Exercise', db.get_engine(app=app), if_exists='replace')

    return app
