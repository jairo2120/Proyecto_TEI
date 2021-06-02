import requests
import json
create_root_user_folder = {
    'id_user':"5646456454"
}

upload_user_file = {
    "id_user":"1216728033",
    "file_name":"secrets.py",
    "path_s3":"",
    "path_local":"/usr/src/folder_management_microservice/code/"
}
create_user_folder = {
    "id_user":"22024414",
    "folder_name":"certificados",
    "path_s3":""
}

delete_user_file = {
    "id_user":"22024414",
    "file_name":"bienvenida.txt",
    "path_s3":"certificados/"
    
}

share_or_copy_file = {
    "id_user_source":"22024414",
    "id_user_destination":"1216728033",
    "path_s3_source":"certificados/microservices.pdf",
    "path_s3_destination":"certificados/microservices.pdf"
}

# share_file = {
#     'upload_file':open('secrets.py','rb')}
# values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
upload_user_file = {
    "id_user":"1216728033",
    "file_name":"eafit.png",
    "path_s3":"",
    "path_local":""
}

#my file to be sent

file = str(upload_user_file['path_local'])+str(upload_user_file['file_name'])


files = [
    ('file', (file, open(file, 'rb'), 'application/octet')),
    ('data_user', ('datas', json.dumps(upload_user_file), 'application/json')),
]

# r = requests.post('http://127.0.0.1:4000/citizen_folder/user',json=create_root_user_folder)
# print(r.status_code)
# r = requests.post('http://52.207.71.206:5001/citizen_folder/folder',json=upload_user_file)
# print(r.status_code)

# r = requests.put('http://127.0.0.1:4000//citizen_folder/folder',json=create_user_folder)
# r.status_code
# r = requests.delete('http://127.0.0.1:4000//citizen_folder/folder',json=delete_user_file)
# r.status_code
# r = requests.post('http://127.0.0.1:4000//citizen_folder/folder/share',json=share_or_copy_file)
# r.status_code

r = requests.post('http://127.0.0.1:4000//citizen_folder/folder',files=files)
print(str(r.content))