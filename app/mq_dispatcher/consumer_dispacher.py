import pika
from colorama import Fore, Back, Style, init

init(autoreset=True)


def on_message_received(ch, method, properties, body):
    print(Fore.BLUE + Back.WHITE + f"Mensaje recibido: {body}")


def init_consumer_dispacher():
    # connection_parameters = pika.ConnectionParameters('localhost')
    # connection = pika.BlockingConnection(connection_parameters)
    # channel = connection.channel()
    # channel.queue_declare(queue='[DISPACHER]', durable=False)
    # channel.basic_consume(queue='[DISPACHER]', auto_ack=True,
    #                       on_message_callback=on_message_received)
    print("starting consuming...")

    # channel.start_consuming()
