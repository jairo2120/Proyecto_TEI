FROM python:3.8-slim-buster

# envioroment api flask 
ENV YOUR_HOST=your_host \
    YOUR_PORT=your_port

# envioroment DB

ENV YOUR_DB_HOST=your_db_host \
    YOUR_DB_USER=your_db_user \
    YOUR_DB_PASS=your_db_pass \
    YOUR_DB=your_db

# enviroment server rabbitmq
ENV SERVER_IP=your_server_ip\
    SERVER_PORT=your_server_port\
    SERVER_USER=your_server_user\
    SERVER_PASSWORD=your_server_password

WORKDIR /usr/src/register-api-microservice
COPY . .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["code/app.py"]
ENTRYPOINT [ "python3" ]

