from flask import request, render_template, make_response, url_for, redirect
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User


@app.route('/')
def home():
    """Landing page."""
    return render_template("home.html",
                           title="Demo home page",
                           description="Description for the homepage"
                           )


@app.route('/users', methods=['GET'])
def user_records():
    """Create a user via quesry string parameters"""
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
        redirect(url_for('user_records'))
    return render_template(
        'users.jinja2',
        users=User.query.all(),
        title="Show Users"
    )
