import boto3 
import os
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_bucket_project = os.getenv('BUCKET_PROJECT')
client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)  


 #AWS_ACCESS_KEY_ID #AWS_SECRET_ACCESS_KEY

def create_root_folder(id_user): 
    client.upload_file(
        "bienvenida.txt",
        aws_bucket_project,
        str(id_user)+"/bienvenida.txt"
    )
    
def create_folder(id_user,name,path_s3):
    client.upload_file(
        "bienvenida.txt",
        aws_bucket_project,
        str(id_user)+"/"+str(name)+"/bienvenida.txt"
    )    


def upload_file(id_user,file_name, path_s3, path_local): 
    client.upload_file(
        str(path_local)+str(file_name),
        aws_bucket_project,
        str(id_user)+"/"+str(path_s3)+str(file_name )
    ) #BUCKET_PROJECT
        
def download_file(id_user,file_name, path_s3, path_local): 
    client.download_file(
        aws_bucket_project,
        str(id_user)+"/"+str(path_s3)+str(file_name),
        str(path_local)+str(file_name)
    )

def delete_file(id_user,file_name, path_s3): 
    client.delete_object(
        Bucket=aws_bucket_project,
        Key=str(id_user)+"/"+str(path_s3)+file_name
    )

def list_directory(id_user):
    response = client.list_objects_v2(
    Bucket=aws_bucket_project,
    Prefix =id_user,
    MaxKeys=1000
    )
    return response['Contents']

def share_or_copy_file(id_user_source, id_user_destination, path_s3_source, path_s3_destination):
    copysource = str(aws_bucket_project)+"/"+str(id_user_source)+"/"+str(path_s3_source)
    key = str(id_user_destination)+"/"+str(path_s3_destination)
    
    client.copy_object(
        Bucket=aws_bucket_project,
        CopySource=copysource,
        Key=key
    )
