import pika

DISPACHER: str = "[DISPACHER]"


def send_order(count: int, code: str, sucursal: str):
    print("ejecutar mensaje")
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue=DISPACHER)
    message = "Se necesita " + \
        str(count)+" unidades del producto con codigo " + \
        str(code)+" en la sucursal "+sucursal+"."
    channel.basic_publish(exchange='', routing_key=DISPACHER, body=message)
    print(f"sent mesagge: {message}")
    connection.close()
