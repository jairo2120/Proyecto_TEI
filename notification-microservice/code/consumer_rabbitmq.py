import pika
from notification_manager import Notification_manager
from sms import sendSms

connection = pika.BlockingConnection(pika.ConnectionParameters(SERVER_IP, SERVER_PORT, '/',
pika.PlainCredentials(SERVER_USER, SERVER_PASSWORD))) #SERVER_IP, SERVER_PORT, SERVER_USER, SERVER_PASSWORD
channel = connection.channel()

def callback(ch, method, properties, body): 
    chain = str(body).split(",")
    email_not_remove = chain[0]
    phone_not_remove = chain[1]
    message_not_remove = chain[2]
    email_remove = email_not_remove.translate({ord(i): None for i in "b'"})
    phone_remove =  phone_not_remove.translate({ord(i): None for i in "'"})
    message_remove =  message_not_remove.translate({ord(i): None for i in "'"})
    notification_manager = Notification_manager(email_remove,phone_remove,message_remove)
    notification_manager.sms_ad()
    notification_manager.email_ad() 
channel.basic_consume(queue=QUEUE, on_message_callback=callback, auto_ack=True) #QUEUE
channel.start_consuming()
