import pika
from os import getenv
from dotenv import load_dotenv

load_dotenv(verbose=True)

params = pika.URLParameters(getenv('AMQP_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()


# publish=producer, 메시지를 어디로 전달시킬것인지
def publish():
    channel.basic_publish(exchange='', routing_key='order', body='hello')
