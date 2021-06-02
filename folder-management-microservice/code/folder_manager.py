from flask import Flask, jsonify, request
from folder_adapter import *
import os
import json
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

your_host = os.getenv('HOST')
your_port = os.getenv('PORT') 

app = Flask(__name__)


@app.route('/citizen_folder/user', methods=['POST'])
def create_root_user_folder():
    user_id = request.json['id_user']
    create_root_folder(user_id)
    return("Welcome")
    
    
@app.route('/citizen_folder/folder/<string:id_user>')
def list_user_directory(id_user):
    try:
        directory = list_directory(id_user)
        return jsonify(directory)       
    except BaseException: 
        return jsonify({"error":"Directory does not exist"})
    
@app.route('/citizen_folder/folder',methods=["PUT"])
def create_user_folder():
    user_id = request.json['id_user']
    folder_name = request.json['folder_name']
    path_s3 = request.json['path_s3']
    create_folder(user_id,folder_name,path_s3)
    return("thanks")

@app.route('/citizen_folder/folder',methods=['POST','GET'])
def upload_user_file():
    file_name = request.files['file']
    file_name.save(secure_filename(file_name.filename))
    user_data= json.load(request.files['data_user'])                                                     
    print(user_data)                                          
    user_id = user_data['id_user']
    file_name = user_data['file_name']
    path_s3 = user_data['path_s3']
    path_local = user_data['path_local']
    upload_file(user_id,file_name,path_s3,path_local)
    os.remove(str(os.path.realpath("."))+"/"+str(path_local)+"/"+str(file_name))
    return (jsonify({"user_id":user_id,"file_name":file_name,"path_local":path_local,"path_s3":path_s3}))

@app.route('/citizen_folder/folder',methods=["DELETE"])
def delete_user_file(): 
    user_id = request.json['id_user']
    file_name = request.json['file_name']
    path_s3 = request.json['path_s3']
    delete_file(user_id,file_name,path_s3)
    return user_id

@app.route('/citizen_folder/folder/share',methods=['POST'])
def share_or_copy_user_file():
    id_user_source = request.json['id_user_source']
    id_user_destination = request.json['id_user_destination']
    path_s3_source = request.json['path_s3_source']
    path_s3_destination = request.json['path_s3_destination']
    share_or_copy_file(id_user_source,id_user_destination,path_s3_source,path_s3_destination)
    return id_user_source
if __name__ == '__main__':
    app.run(debug=True,host=your_host,port=your_port)