# TODO
# Get framework for each app page setup (i.e. get blueprints working)
# Load excel data into DB
# Create exercise, workout classes that work with data in the DB

# Finish tutorial, start pull request in git to merge with master / understand process


import os

from flask import Flask


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
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

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db    # register db initialization function with the app
    db.init_app(app)

    from views import auth
    app.register_blueprint(auth.bp)

    from . import views
    app.register_blueprint(views.bp)

    return app
