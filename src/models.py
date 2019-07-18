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
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    searchRequests = db.Column(db.Integer, unique=False, nullable=False)
    findings = db.Column(db.Integer, unique=False, nullable=False)
    photo = db.Column(db.String(300), unique=False, nullable=True)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Lost(db.Model):
    __tablename__ = 'lost'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Lost %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Finded(db.Model):
    __tablename__ = 'finded'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Finded %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

render_er(db.Model, 'diagram.png')