FROM python:3 
WORKDIR  /usr/src/sms 
COPY . . 
RUN pip3 install clx-sdk-xms
RUN pip3 install pika
CMD ["consumidorrabbitmq.py"]
ENTRYPOINT [ "python3" ]
