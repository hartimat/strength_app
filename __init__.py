# TODO
# Load excel data into DB, connect to application
# Create exercise, workout classes that work with data in the DB
# Create pages for the app (create exercises, create workouts, load past workouts, progress dashboard)
# CSS / formatting (bootstrap?)
# Pull request in git to understand the process


import os

from flask import Flask


def create_app(test_config=None):
    # Create application
    app = Flask(__name__, instance_relative_config=True)

    # Configure application
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize database
    from . import db    # register db initialization function with the core
    db.init_app(app)

    # Register blueprints
    from .views.auth import auth
    app.register_blueprint(auth)
    from .views.core import core
    app.register_blueprint(core)

    return app
