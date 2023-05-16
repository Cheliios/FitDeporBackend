from flask import Flask, jsonify, request, render_template,redirect,session
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_claims
)
from src.controllers.userController import userController
import os
import hashlib


app = Flask(__name__)
app.secret_key = "any random string"
app.config['JWT_SECRET_KEY'] = 'cambiar_no_olvidar' 
app.config["IMAGE_UPLOADS"] = "/tmp"
jwt = JWTManager(app)

#CRUD
# Read leer listar obtener  -> GET

@app.route('/users', methods=['GET'])
def get_users():
    return userController().get_users()

# CREATE insetar agregar  -> POST
@app.route('/users', methods=['POST'])
def add_users():
    return userController().add_users(request)

# Modificar actualizar update -> PUT
@app.route('/users', methods=['PUT'])
def update_users():
    return userController().update_users(request)

# URL/user/1
# eliminar delete -> DELETE
@app.route('/users/<index>', methods=['DELETE'])
def delete_users(index):
    return userController().delete_users(index)

# URL/user/1
# Objeter dato exacto
@app.route('/users/<index>', methods=['GET'])
def get_users_by_id(index):
    return userController().get_users_by_id(index)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

