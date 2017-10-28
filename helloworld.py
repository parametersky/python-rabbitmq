import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_public(exchange='',routing_key='hello',body='hello world')
print(" [x] send 'hello world'")
connection.close()

