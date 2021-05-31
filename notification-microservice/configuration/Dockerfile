FROM python:3 



# Install tools required for project
RUN apt-get update && upgrade \
    pip3 install requests  \
    pip3 install clx-sdk-xms  \
    pip3 install pika

# enviroment server rabbitmq 
ENV SERVER_IP=your_server_ip \
    SERVER_PORT=your_server_port \
    SERVER_USER=your_server_user \
    SERVER_PASSWORD=your_server_password \
    QUEUE=your_queue

# envioroment api sms
ENV SERVICE_PLAN_ID=your_server_id \
    TOKEN=your_token


WORKDIR  /usr/src/notification_microservice
COPY ../ /usr/src/notification_microservice/

CMD ["configuration/enviorement_variable.env","code/consumer_rabbitmq.py"]
ENTRYPOINT ["sh","python3"]
