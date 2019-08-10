from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from datetime import datetime
db = SQLAlchemy()

class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data= db.Column(db.LargeBinary)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    firstname = db.Column(db.String(80), unique=True, nullable=True)
    lastname = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(20), unique=True, nullable=True)
    photo = db.Column(db.String(300), unique=False, nullable=True)
    bank = db.Column(db.String(20), nullable=True)
    accountNum = db.Column(db.String(20), nullable=True)
    accounType = db.Column(db.String(20), nullable=True)
    rut = db.Column(db.String(20), nullable=True)
    adverts = db.relationship('Adverts')

    def __repr__(self):
        return '<User %r>' % self.username
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
        }

class Pets(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=True)
    breed = db.Column(db.String(80), unique=True, nullable=True)
    gender = db.Column(db.String(80), unique=True, nullable=True)
    size = db.Column(db.String(120), unique=True, nullable=True)
    photo = db.Column(db.String(300), unique=False, nullable=True)
    adverts = db.relationship('Adverts')
    def __repr__(self):
        return '<Pets %r>' % self.id
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id,
            "breed": self.breed,
            "gender": self.id,
            "size": self.size}

class Adverts(db.Model):
    __tablename__ = 'adverts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    description = db.Column(db.String(80), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    status = db.Column(db.String(80), unique=False, nullable=True)
    address = db.Column(db.String(80), unique=False, nullable=True)
    def __repr__(self):
        return '<Adverts %r>' % self.id
    def serialize(self):
        return {
            "user_id": self.user_id,
            "pet_id": self.pet_id,
            "status": self.status,
            "created_at": self.created_at
        }

render_er(db.Model, 'diagram.png')