FROM python:3 
WORKDIR  /usr/src/sms 
COPY . . 
RUN sudo apt update
RUN sudo apt install python3-pip
RUN pip3 install -r requirements.txt
RUN pip3 install clx-sdk-xms
RUN pip3 install pika
CMD ["consumidorrabbitmq.py"]
ENTRYPOINT [ "python3" ]
