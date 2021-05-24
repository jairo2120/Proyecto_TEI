FROM python:3 
WORKDIR  /usr/src/sms 
COPY . . 
RUN pip install -r requirements.txt
RUN pip install clx-sdk-xms
RUN pip install pika
CMD ["consumidorrabbitmq.py"]
ENTRYPOINT [ "python3" ]
