import pika
from sms import sendSms
connection = pika.BlockingConnection(pika.ConnectionParameters('52.91.140.110', 5672, '/',
pika.PlainCredentials("guest", "guest")))
channel = connection.channel()
def callback(ch, method, properties, body):
    chain = str(body).split(",")
    phone_not_remove = chain[0]
    message_not_remove = chain[1]
    
    phone_remove = phone_not_remove.translate({ord(i): None for i in "b'"})
    message_remove =  message_not_remove.translate({ord(i): None for i in "'"})
    sendSms(phone_remove,message_remove)
    print(phone_remove,message_remove)
channel.basic_consume(queue="sms", on_message_callback=callback, auto_ack=True)
channel.start_consuming()