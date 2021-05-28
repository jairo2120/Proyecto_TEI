import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(SERVER_IP, SERVER_PORT, '/',
pika.PlainCredentials(SERVER_USER,SERVER_PASSWORD))) #SERVER_IP, SERVER_PORT, SERVER_USER, SERVER_PASSWORD
channel = connection.channel()
channel.basic_publish(exchange='sms', routing_key='test', body=body) #EXCHANG,E ROUTING_KEY,   #body example (email,phone,message)
print("Runnning Producer Application...")
print(" [x] Sent 'Hello World...!'")
connection.close() 