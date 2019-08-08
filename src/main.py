"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, User, Adverts, Pets

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['POST', 'GET', 'DELETE'])
def handle_person():
    """
    Create person and retrieve all persons
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'username' not in body:
            raise APIException('You need to specify the username', status_code=400)
        if 'email' not in body:
            raise APIException('You need to specify the email', status_code=400)

        user1 = User(username=body['username'], email=body['email'])
        db.session.add(user1)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        all_people = User.query.all()
        all_people = list(map(lambda x: x.serialize(), all_people))
        return jsonify(all_people), 200

    if request.method == 'DELETE':
        delete_all= User.query().delete()
        db.session.delete(delete_all)
        return jsonify(delete_all), 200

    return "Invalid Method", 404

@app.route('/pets', methods=['GET'])
def handle_pets():
    """
    Create person and retrieve all persons
    """
    # GET request
    if request.method == 'GET':
        all_pets = Pets.query.all()
        all_pets = list(map(lambda x: x.serialize(), all_pets))

        return jsonify(all_pets), 200

    return "Invalid Method", 404





@app.route('/adverts', methods=['POST', 'GET'])

def handle_adverts():
    """
    Create ad and retrieve all ads
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'status' not in body:
            raise APIException('You need to specify the pet name', status_code=400)

        pet1 = Pets(name=body['name'])
        db.session.add(pet1)
        db.session.commit()

        petId=Pets

        request1 = Adverts(status=body['status'], pet_id=body['pet_id'], user_id=body['user_id'])
        db.session.add(request1)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        status = request.args.get('status')
        all_adverts = Adverts.query.filter_by(status=status).order_by(Adverts.created_at.desc())
        all_adverts = list(map(lambda x: x.serialize(), all_adverts))

        return jsonify(all_adverts), 200

    """if request.method == 'GET':
        all_adverts = db.session.query(Adverts).join(Pets).all()
        all_adverts = list(map(lambda x: x.serialize(), all_adverts))

        return jsonify(all_adverts), 200"""

    return "Invalid Method", 404

@app.route('/user/<int:user_id>', methods=['PUT', 'GET', 'DELETE'])
def get_single_person(user_id):
    """
    Single person
    """

    # PUT request
    if request.method == 'PUT':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)

        user1 = User.query.get(user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)

        if "username" in body:
            user1.username = body["username"]
        if "email" in body:
            user1.email = body["email"]
        db.session.commit()

        return jsonify(user1.serialize()), 200

    # GET request
    if request.method == 'GET':
        user1 = User.query.get(user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        return jsonify(user1.serialize()), 200

    # DELETE request
    if request.method == 'DELETE':
        user1 = User.query.get(user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        db.session.delete(user1)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
