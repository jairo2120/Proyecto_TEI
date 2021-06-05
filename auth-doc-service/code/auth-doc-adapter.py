from flask import Flask, jsonify, request
import urllib.request, urllib.parse, json

def getDoc(id, UrlDocument, documentTitle):
    verifyDoc = 'govcarpetaapp.mybluemix.net/apis/'+str(id)+'/'+str(UrlDocument)+'/'+str(documentTitle)
    response = urllib.request.urlopen(verifyDoc)
    return response.read()