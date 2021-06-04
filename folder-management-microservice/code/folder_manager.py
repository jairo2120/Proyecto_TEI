from flask import Flask, jsonify, request, send_from_directory
from folder_adapter import *
import os
import json
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import shutil

your_host = os.getenv('HOST')
your_port = os.getenv('PORT') 

app = Flask(__name__)


@app.route('/citizen_folder/user', methods=['POST'])
def create_root_user_folder():
    try:
        user_id = request.json['id_user']
        if user_id != "":
            create_root_folder(user_id)
            return(jsonify({"menssage":"ok!"}))
        else: 
           return(jsonify({"menssage":"contains no id_user"}))
    except Exception as e:
        return (jsonify({"error":str(e)}))
    
    
@app.route('/citizen_folder/folder/<string:id_user>')
def list_user_directory(id_user):
    try:
        directory = list_directory(id_user)
        return jsonify(directory)       
    except Exception as e: 
        return (jsonify({"error":str(e)}))
    
@app.route('/citizen_folder/folder',methods=["PUT"])
def create_user_folder():
    try:
        user_id = request.json['id_user']
        folder_name = request.json['folder_name']
        path_s3 = request.json['path_s3']
        if (user_id and folder_name) != "": 
            create_folder(user_id,folder_name,path_s3)
            return(jsonify({"menssage":"ok!"}))
        else: 
            return(jsonify({"menssage":"missing some parameter"}))
    except Exception as e: 
        return (jsonify({"error":str(e)}))

@app.route('/citizen_folder/folder',methods=['POST','GET'])
def upload_user_file():
    try:
        
        file_name = request.files['file']
        file_name.save(secure_filename(file_name.filename))
        user_data= json.load(request.files['data_user'])                                                                                             
        user_id = user_data['id_user']
        file_name = user_data['file_name']
        path_s3 = user_data['path_s3']
        path_local = user_data['path_local']
        if (user_id and file_name) != "":
            upload_file(user_id,file_name,path_s3,path_local)
            os.remove(str(os.path.realpath("."))+"/"+str(path_local)+"/"+str(file_name))
            return (jsonify({"user_id":user_id,"file_name":file_name,"path_local":path_local,"path_s3":path_s3}))
        else: 
            return(jsonify({"menssage":"missing some parameter"}))
    except Exception as e: 
        return (jsonify({"error":str(e)}))

@app.route('/citizen_folder/folder',methods=["DELETE"])
def delete_user_file(): 
    try: 
        user_id = request.json['id_user']
        file_name = request.json['file_name']
        path_s3 = request.json['path_s3']
        if(user_id and file_name) == "":
            delete_file(user_id,file_name,path_s3)
            return "ok!"
        else:
            return(jsonify({"menssage":"missing some parameter"}))
    except Exception as e: 
        return (jsonify({"error":str(e)}))

@app.route('/citizen_folder/folder/share',methods=['POST'])
def share_or_copy_user_file():
    try:
        id_user_source = request.json['id_user_source']
        id_user_destination = request.json['id_user_destination']
        path_s3_source = request.json['path_s3_source']
        path_s3_destination = request.json['path_s3_destination']
        if(id_user_source and id_user_destination and path_s3_source and path_s3_destination) != "":
            share_or_copy_file(id_user_source,id_user_destination,path_s3_source,path_s3_destination)
            return (jsonify({"mensaje":"ok!"}))
        else:
            return(jsonify({"menssage":"missing some parameter"}))
    except Exception as e: 
        return (jsonify({"error":str(e)}))

@app.route('/citizen_folder/folder/dowload', methods=['GET'])
def dowload_user_file():
    shutil.rmtree('prueba', ignore_errors=True)
    os.mkdir("prueba")
    try:                                                                                              
        user_id = request.args.get('id_user')
        file_name = request.args.get('file_name')
        path_s3 = request.args.get('path_s3')
        path_local = request.args.get('path_local')
        if (user_id and file_name) != "":
            download_file(user_id,file_name,path_s3,path_local)
            return send_from_directory("prueba/", str(path_local)+str(file_name), as_attachment=True)
        return(jsonify({"menssage":"missing some parameter"}))
    except Exception as e: 
        return (jsonify({"error":str(e)}))
    

if __name__ == '__main__':
    app.run(debug=True,host=your_host,port=your_port) #host=your_host