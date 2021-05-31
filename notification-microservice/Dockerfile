
FROM python:3.8-slim-buster

# Install tools required for project

# enviroment server rabbitmq
ENV SERVER_IP=your_server_ip\
    SERVER_PORT=your_server_port\
    SERVER_USER=your_server_user\
    SERVER_PASSWORD=your_server_password\

# envioroment api sms
ENV SERVICE_PLAN_ID=your_service_plan_id \
    TOKEN=your_token

WORKDIR  /usr/src/notification_microservice
COPY . .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["code/consumer_rabbitmq.py"]
ENTRYPOINT ["python3"]

