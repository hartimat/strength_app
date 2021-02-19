"""Data models"""
from . import db


class User(db.Model):
    """Data model for user accounts"""

    __tablename__ = 'User'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    bio = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Exercise(db.Model):
    """Data model for exercises"""

    __tablename__ = 'Exercise'
    index = db.Column(
        db.Integer,
        primary_key=True
    )
    date = db.Column(
        db.String,
        index=False,
        unique=False,
        nullable=False
    )
    name = db.Column(
        db.String(80),
        index=False,
        unique=False,
        nullable=False
    )
    sets = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=True
    )
    reps = db.Column(
        db.String(80),
        index=False,
        unique=False,
        nullable=True
    )
    weight = db.Column(
        db.Float,
        index=False,
        unique=False,
        nullable=True
    )
    rest = db.Column(
        db.Float,
        index=False,
        unique=False,
        nullable=True
    )
    notes = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )

    def __repr__(self):
        return '<Exercise {}>'.format(self.name)

    def __init__(self, id, date, name, sets, reps, weight, rest, notes):
        self.id = id
        self.date = date
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.rest = rest
        self.notes = notes
