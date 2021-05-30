from secrets import access_key, secret_access_key
import boto3 
import os 

client = boto3.client('s3', aws_access_key_id='AKIA6CB3TLHF7EN2SRPA', aws_secret_access_key='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')

# for file in os.listdir():
#     if  '.py' in file: 
#         upload_file_bucket = 'tei-bucket-eafit'
#         upload_file_key = 'tei-bucket-eafit/'+str(file)
#         client.upload_file(file,upload_file_bucket,upload_file_key)
#         output = f"downloads/{file_name}"
#client.download_file("tei-bucket-eafit","Figure_2.png","prueba/Figure_2.png")

# identificacion = input("Ingrese su identificacion")
# contrasena = input("Ingrese la contrasena")
# client.upload_file("prueba.txt","tei-bucket-eafit",str(identificacion)+"/prueba.txt")
#client.delete_object(Bucket="tei-bucket-eafit",key="Figure_2.png")
# all_objects = client.list_objects(Bucket = 'tei-bucket-eafit') 
# print(all_objects)
# response = client.list_objects_v2(
#     Bucket="tei-bucket-eafit",
#     Prefix ='22024414',
#     MaxKeys=100 )
# print(response['Contents'])

response = client.copy_object(Bucket='tei-bucket-eafit',CopySource='tei-bucket-eafit/22024414/Figure_2.png',Key='1216728033/Figure_2.png')
print(response)