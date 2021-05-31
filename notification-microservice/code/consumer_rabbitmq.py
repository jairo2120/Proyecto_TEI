import pika
from notification_manager import Notification_manager
import os

your_server_ip=os.getenv('SERVER_IP')
your_server_port = os.getenv('SERVER_PORT')
your_server_user = os.getenv('SERVER_USER')
your_server_pass = os.getenv('SERVER_PASS')
your_server_queue = os.getenv('SERVER_QUEUE')

connection = pika.BlockingConnection(pika.ConnectionParameters(your_server_ip, your_server_port, '/',
pika.PlainCredentials(your_server_user,your_server_pass))) #SERVER_IP, SERVER_PORT, SERVER_USER, SERVER_PASSWORD
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
channel.basic_consume(queue=your_server_queue, on_message_callback=callback, auto_ack=True) #QUEUE
channel.start_consuming()