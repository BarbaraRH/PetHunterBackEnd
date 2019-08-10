import os
from flask import Flask, request, jsonify, url_for, render_template
from werkzeug import secure_filename
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, User, Adverts, Pets
app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['UPLOAD_FOLDER'] = "./upload"

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

@app.route('/upload', methods=['GET', 'POST'])#ruta guardar fotos
def upload():
    # GET request
    if request.method == 'POST':
        f= request.file["file"]
        filename=secure_filename(f.filename)
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return "subido con exito"




@app.route('/users', methods=['POST', 'GET', 'DELETE'])
def handle_person():
    # POST request
    if request.method == 'POST':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'username' not in body:
            raise APIException('You need to specify the username', status_code=400)
        if 'email' not in body:
            raise APIException('You need to specify the email', status_code=400)
        if 'password' not in body:
            raise APIException('You need to specify the password', status_code=400)
        if 'firstname' not in body:
            raise APIException('You need to specify the firstname', status_code=400)
        if 'lastname' not in body:
            raise APIException('You need to specify the lastname', status_code=400)
        user1 = User(username=body['username'], email=body['email'], password=body['password'], firstname=body['firstname'], lastname=body['lastname'])
        db.session.add(user1)
        db.session.commit()
        return "ok", 200
    # GET request
    if request.method == 'GET':
        all_people = User.query.all()
        all_people = list(map(lambda x: x.serialize(), all_people))
        return jsonify(all_people), 200
     # DELETE request
    if request.method == 'DELETE':
        db.session.query(User).delete()
        db.session.commit()
        return "all Deleted", 200
    return "Invalid Method", 404
@app.route('/pets', methods=['GET', 'DELETE'])
def handle_pets():
    # GET request
    if request.method == 'GET':
        all_pets = Pets.query.all()
        all_pets = list(map(lambda x: x.serialize(), all_pets))
        return jsonify(all_pets), 200
     # DELETE request
    if request.method == 'DELETE':
        db.session.query(Pets).delete()
        db.session.commit()
        return "all Deleted"
@app.route('/adverts', methods=['POST', 'GET','DELETE', 'UPDATE'])
def handle_adverts():
    # POST request
    if request.method == 'POST':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
       # if 'status' not in body:
        #    raise APIException('You need to specify the status', status_code=400)

        #request1 = Pets(name=body['name'])
        #db.session.add(request1)
        #db.session.commit()

        #query_the_last_pets= Pets.query.order_by(Pets.id.desc()).first()

        #request2 = Adverts(status=body['status'])
        #db.session.add(request2)
        #db.session.commit()

        request1 = Adverts(status=body['status'])
        request2 = Pets(name=body['name'])
        request2.adverts.append(request1)
        db.session.add(request2)
        db.session.commit()
        #Adverts.update().where(Adverts.c.pet_id==null).values(pet_id=query_the_last_pets)

        return str("ok")#query_the_last_pets.id
    # GET request
    if request.method == 'GET':
        status = request.args.get('status')
        all_adverts = Adverts.query.filter_by(status=status).order_by(Adverts.created_at.desc())
        all_adverts = list(map(lambda x: x.serialize(), all_adverts))
        return jsonify(all_adverts), 200
        # DELETE request
    if request.method == 'DELETE':
        db.session.query(Adverts).delete()
        db.session.commit()
        return "all Deleted"
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