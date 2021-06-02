FROM python:3.8-slim-buster

# envioroment api flask 
ENV HOST=your_host \
    PORT=your_port

# envioroment s3

ENV AWS_ACCESS_KEY_ID=aws_access_key_id \
    AWS_SECRET_ACCESS_KEY=aws_secret_access_key\
    BUCKET_PROJECT=aws_bucket_project

WORKDIR /usr/src/folder_management_microservice
COPY . .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["code/folder_manager.py"]
ENTRYPOINT [ "python3" ]

