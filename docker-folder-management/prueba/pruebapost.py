import requests

create_root_user_folder = {
    'id_user':"22024414"
}

upload_user_file = {
    "id_user":"22024414",
    "file_name":"prueba.txt",
    "path_s3":"certificados/",
    "path_local":""
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
# r = requests.post('http://127.0.0.1:4000//citizen_folder/user',json=create_root_user_folder)
# r.status_code
# r = requests.post('http://127.0.0.1:4000//citizen_folder/folder',json=upload_user_file)
# r.status_code

# r = requests.put('http://127.0.0.1:4000//citizen_folder/folder',json=create_user_folder)
# r.status_code
# r = requests.delete('http://127.0.0.1:4000//citizen_folder/folder',json=delete_user_file)
# r.status_code
r = requests.post('http://127.0.0.1:4000//citizen_folder/folder/share',json=share_or_copy_file)
r.status_code
