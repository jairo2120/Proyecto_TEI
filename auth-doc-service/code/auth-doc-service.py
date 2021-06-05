from flask import Flask, jsonify, request

app = Flask(__name__)

from adapter_centralizador import getDoc
import os

your_host = os.getenv('YOUR_HOST')
your_port = os.getenv('YOUR_PORT')

#verificacion usuario
@app.route('/users/<int:id>/<string:UrlDocument>/<string:documentTitle>')
def authDoc(id, UrlDocument, documentTitle):
    return getDoc(id, UrlDocument, documentTitle)

if __name__ == '__main__':
    app.run(debug=True, host=your_host, port=your_port)