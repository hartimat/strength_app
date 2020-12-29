# TODO
# Load excel data into DB, connect to application
# Create exercise, workout classes that work with data in the DB
# Create pages for the app (create exercises, create workouts, load past workouts, progress dashboard)
# CSS / formatting (bootstrap?)
# Create a new dev branch where pandas is used instead of sqlite
# Pull request in git to understand the process
# Basic version tagging, development branching work processes in Git
# Dig into how to use python click library


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis


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
        # Include routes
        from . import routes

        # Register blueprints
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(admin.admin_bp)

    return app
