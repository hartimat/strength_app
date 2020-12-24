import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db

bp = Blueprint('views', __name__, url_prefix='/views')


@bp.route('/index')
def index():
    return render_template('index.html')
