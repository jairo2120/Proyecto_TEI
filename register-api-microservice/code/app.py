from flask import Flask, jsonify, request

app = Flask(__name__)

from adapterBD import addnewUser, consultarUser
from adapter_centralizador import getCitizen, getDoc, registerCitizen, senderrorSMS
import mysql
import os

your_host = os.getenv('YOUR_HOST')
your_port = os.getenv('YOUR_PORT')

@app.route('/users/<int:id>')
def getUser(id):
    # print(getCitizen(id_num))

    if getCitizen(id) == b'':
        return jsonify({"message": "User not found"})
    else:
        #consultarUser(id)
        return getCitizen(id)

@app.route('/users/addCitizen', methods=['POST'])
def addUser():
    new_user = {
        "id": request.json['id'],
        "id_type": request.json['id_type'],
        "name": request.json['name'],
        "address": request.json['address'],
        "email": request.json['email'],
        "telephone": request.json['telephone'],
        "bool_emp": request.json['bool_emp'],
        "operatorId": request.json['operatorId'],
        "operatorName": request.json['operatorName']
    }
    if getCitizen(new_user['id']) == b'':
        try:

            if addnewUser(
                new_user['id'],
                new_user['id_type'],
                new_user['name'],
                new_user['address'],
                new_user['email'],
                new_user['telephone'],
                new_user['bool_emp'],
                new_user['operatorId'],
                new_user['operatorName']
                ):
                registerCitizen(new_user)
                return (jsonify({"Exito de registro":"Usuario creado con exito"}))
        except:
            return (jsonify({"Error de registro":"Usuario ya existe con id:"+str(new_user['id'])}))
    else:
        senderrorSMS(new_user['email'], new_user('telephone'))
        return getCitizen(id)

@app.route('/users/login/<int:id>')
def login(id):
    #return getCitizen(id)
    if consultarUser(id):
        return(jsonify({"Login message": "Bienvenido!"}))
    else:
        return(jsonify({"Error message": "Datos erroneos"}))

if __name__ == '__main__':
    app.run(debug=True, host=your_host, port=your_port)
