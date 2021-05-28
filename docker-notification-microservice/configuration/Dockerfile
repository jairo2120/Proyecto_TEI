FROM python:3 

# Install tools required for project
RUN apt-get update && upgrade \
    pip3 install requests  \
    pip3 install clx-sdk-xms  \
    pip3 install pika

WORKDIR  /usr/src/notification_microservice
COPY ../ /usr/src/notification_microservice/

CMD ["configuration/enviorement_variable.env","code/consumer_rabbitmq.py"]
ENTRYPOINT ["sh","python3"]
