from flask import Flask, jsonify, request, render_template,redirect,session
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_claims
)
from src.controllers.userController import userController
import os
import hashlib

# cambio
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import SimpleConnectionPool
from src.cn.data_base_connection import Database


app = Flask(__name__)
app.secret_key = "any random string"
app.config['JWT_SECRET_KEY'] = 'cambiar_no_olvidar' 
app.config["IMAGE_UPLOADS"] = "/tmp"
jwt = JWTManager(app)

#cambio1
db = Database()

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



@app.route('/register', methods=['POST', 'GET'])
def register():
    user_nickname = request.form.get('user_nickname')
    user_password = request.form.get('user_password')
    user_name = request.form.get('user_name')
    user_lastname = request.form.get('user_lastname')
    user_edad = request.form.get('user_edad')
    user_genero = request.form.get('user_genero')
    user_pais = request.form.get('user_pais')
    user_mail = request.form.get('user_mail')

    # Verificar si el nickname ya está registrado en la base de datos
    db.connect(host='35.225.144.32', port=5432, user='certus_joche', password='joche123', database='certus_db')
    db.set_cursor()
    db.get_cursor().execute("SELECT * FROM main.user_app WHERE user_nickname = %s", (user_nickname,))
    result = db.get_cursor().fetchone()

    if result is not None:
        db.disconnect()
        return 'El nickname ya está registrado' 

    # Insertar el nuevo usuario en la base de datos
    db.get_cursor().execute("INSERT INTO main.user_app (user_nickname, user_password, user_name, user_lastname, user_edad, user_genero, user_pais, user_mail) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (user_nickname, user_password, user_name, user_lastname, user_edad, user_genero, user_pais, user_mail))
    db.get_client().commit()
    db.disconnect()

    return 'OK'  # Registro exitoso



@app.route('/login', methods=['POST', 'GET'])
def login():
    user_nickname = request.form.get('user_nickname')
    user_password = request.form.get('user_password')

    # Verificar si los datos coinciden en la base de datos
    db.connect(host='35.225.144.32', port=5432, user='certus_joche', password='joche123', database='certus_db')
    db.set_cursor()
    db.get_cursor().execute("SELECT * FROM main.user_app WHERE user_nickname = %s AND user_password = %s", (user_nickname, user_password))
    result = db.get_cursor().fetchone()
    db.disconnect()

    if result is None:
        return 'Usuario no encontrado o contraseña incorrecta'

    return 'OK'  # Login exitoso




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

