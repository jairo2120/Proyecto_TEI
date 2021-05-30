from flask import Flask, jsonify, request
from folder_adapter import *

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

@app.route('/citizen_folder/folder',methods=['POST'])
def upload_user_file():
    print(request.json)
    user_id = request.json['id_user']
    file_name = request.json['file_name']
    path_s3 = request.json['path_s3']
    path_local = request.json['path_local']
    upload_file(user_id,file_name,path_s3,path_local)
    return user_id

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
    app.run(debug=True, port=4000)