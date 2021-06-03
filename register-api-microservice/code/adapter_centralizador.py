from flask import Flask, jsonify, request
from users import users
import urllib.request, urllib.parse, json
import pika
import os
your_server_ip = os.getenv()
your_server_port = os.getenv()
your_server_user = os.getenv()
your_server_password = os.getenv()


def getDoc(id, UrlDocument, documentTitle):
    verifyDoc = 'govcarpetaapp.mybluemix.net/apis/'+str(id)+'/'+str(UrlDocument)+'/'+str(documentTitle)
    response = urllib.request.urlopen(verifyDoc)
    return response.read()
    return requests.get(verifyDoc).content

def getCitizen(id_num):
    #userFound = [user for user in users if user["id_num"] == id_num]
    verifyCitizen = 'https://govcarpetaapp.mybluemix.net/apis/validateCitizen/'+str(id_num)
    response = urllib.request.urlopen(verifyCitizen)
    return response.read()

def registerCitizen(new_user):
    url = 'https://govcarpetaapp.mybluemix.net/apis/registerCitizen'
    
    data = json.dumps(new_user)
    headers = {"Content-Type":"application/json; charset=UTF-8"}
    
    req = urllib.request.Request(url, data = bytes(data.encode("utf-8")), headers=headers)
    resp = urllib.request.urlopen(req)
    sendSMS(new_user['email'], new_user['telephone'])
    print(resp.read())

def sendSMS(email, telephone):
    connection = pika.BlockingConnection(pika.ConnectionParameters(your_server_ip,your_server_port,'/',
    pika.PlainCredentials(your_server_user,your_server_password))) #SERVER_IP, SERVER_PORT, SERVER_USER, SERVER_PASSWORD
    channel = connection.channel()
    channel.basic_publish(exchange='sms', routing_key='test', body=(str(email)+", "+str(telephone)+", Registrado con exito")) #EXCHANG,E ROUTING_KEY,   #body example (email,phone,message)
    print("Runnning Producer Application...")
    print(" [x] Sent 'Hello World...!'")
    connection.close()

def senderrorSMS(email, telephone):
    connection = pika.BlockingConnection(pika.ConnectionParameters(your_server_ip,your_server_port,'/',
    pika.PlainCredentials(your_server_user,your_server_password))) #SERVER_IP, SERVER_PORT, SERVER_USER, SERVER_PASSWORD
    channel = connection.channel()
    channel.basic_publish(exchange='sms', routing_key='test', body=(str(email)+", "+str(telephone)+", No es posible registrarse")) #EXCHANG,E ROUTING_KEY,   #body example (email,phone,message)
    print("Runnning Producer Application...")
    print(" [x] Sent 'Hello World...!'")
    connection.close()

        