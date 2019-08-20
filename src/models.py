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
    data = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<Photo %r>' % self.name
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    firstname = db.Column(db.String(80), unique=False, nullable=True)
    lastname = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(20), unique=False, nullable=True)
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
            "email": self.email,
            "password": self.password,
        }

class Pets(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    breed = db.Column(db.String(80), unique=False, nullable=True)
    gender = db.Column(db.String(80), unique=False, nullable=True)
    size = db.Column(db.String(120), unique=False, nullable=True)
    photo = db.Column(db.String(300), unique=False, nullable=True)
    chip_num = db.Column(db.Integer, nullable=True)
    adverts = db.relationship('Adverts')

    def __repr__(self):
        return '<Pets %r>' % self.id

    def serialize(self):
        return {
            "name": self.name,
            "id": self.id,
            "breed": self.breed,
            "gender": self.gender,
            "size": self.size,
            "chip_num": self.chip_num
        }

class Adverts(db.Model):
    __tablename__ = 'adverts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    description = db.Column(db.String(80), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    status = db.Column(db.String(80), unique=False, nullable=True)
    address = db.Column(db.String(80), unique=False, nullable=True)
    city = db.Column(db.String(80), unique=False, nullable=True)
    district = db.Column(db.String(80), unique=False, nullable=True)
    street1 = db.Column(db.String(80), unique=False, nullable=True)
    street2 = db.Column(db.String(80), unique=False, nullable=True)
    photo_url = db.Column(db.String(200), unique=False, nullable=True)

    def __repr__(self):
        return '<Adverts %r>' % self.id

    def serialize(self):
        return {
            "user_id": self.user_id,
            "pet_id": self.pet_id,
            "status": self.status,
            "created_at": self.created_at,
            "city": self.city,
            "district": self.district,
            "street1": self.street1,
            "street2": self.street2,
            "photo_url": self.photo_url
        }

render_er(db.Model, 'diagram.png')
