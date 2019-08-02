from flask_sqlalchemy import SQLAlchemy

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=True)
    photo = db.Column(db.String(300), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "id": self.id
        }

class Pets(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=True)
    breed = db.Column(db.String(80), unique=True, nullable=True)
    gender = db.Column(db.String(80), unique=True, nullable=True)
    size = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(300), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "id": self.id
        }

class Adverts(db.Model):
    __tablename__ = 'adverts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    description = db.Column(db.String(80), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=False, nullable=False)
    status = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return 'Adverts %r>' % self.id

    def serialize(self):
        return {
            "user_id": self.user_id,
            "status": self.status
        }

render_er(db.Model, 'diagram.png')