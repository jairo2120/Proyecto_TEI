from flask import Flask, jsonify, request

app = Flask(__name__)

from adapterBD import addnewUser, consultarUser, loginUser
from adapter_centralizador import getCitizen, registerCitizen, senderrorSMS
import mysql 
import os

your_host = os.getenv('YOUR_HOST')
your_port = os.getenv('YOUR_PORT')  

#verificacion usuario
@app.route('/users/<int:id>')
def getUser(id):
    # print(getCitizen(id_num))

    if getCitizen(id) == b'':
        if consultarUser(id):
            return jsonify({"User partially found": "Usuario en BD de operador, pero no en centralizador"})
        else:
            return jsonify({"User not found": "Usuario no registrado ni en nuestro operador ni en govcarpeta"})
    else:
        return getCitizen(id)

#registro de usuario
@app.route('/users/addCitizen', methods=['POST'])
def addUser():
    #obtener datos de front
    new_user = {
        "id": request.json['id'],
        "password": request.json['password'],
        "id_type": request.json['id_type'],
        "name": request.json['name'],
        "address": request.json['address'],
        "email": request.json['email'],
        "telephone": request.json['telephone'],
        "bool_emp": request.json['bool_emp'],
        "operatorId": request.json['operatorId'],
        "operatorName": request.json['operatorName']
    }
    #verificar con centralizador
    if getCitizen(new_user['id']) == b'':
        try:
            #intentar registrar en BD de nuestro operador            
            if addnewUser(
                new_user['id'],
                new_user['password'], 
                new_user['id_type'], 
                new_user['name'], 
                new_user['address'],
                new_user['email'],
                new_user['telephone'],
                new_user['bool_emp'],
                new_user['operatorId'],
                new_user['operatorName']
                ):
                #registrar el usuario con nuestro operador en centralizador
                registerCitizen(new_user)
                return (jsonify({"Exito de registro":"Usuario creado con exito en nuestro operador"}))
            else:
                senderrorSMS(new_user['email'], new_user('telephone'))
                #registrar el usuario con nuestro operador en centralizador
                registerCitizen(new_user)
                return (jsonify({"Register failed":"Hubo un error al registrar el usuario en nuestro operador"}))
        except:
            senderrorSMS(new_user['email'], new_user('telephone'))
            return (jsonify({"Error de registro":"Error al registrar usuario en la BD de nuestro operador"}))
    else:
        senderrorSMS(new_user['email'], new_user('telephone'))
        return getCitizen(id)

#login al operador
@app.route('/users/login/<int:id>/<string:password>')
def login(id, password):
    #return getCitizen(id)
    if loginUser(id, password):
        return(jsonify({"Login message": "Bienvenido!"}))
    else:
        return(jsonify({"Error message": "Datos erroneos"}))

if __name__ == '__main__':
    app.run(debug=True, host=your_host, port=your_port)
