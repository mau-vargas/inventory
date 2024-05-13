import pika

SUPPLY: str = "[SUPPLY]"


def execute_order(count: int, code: str, sucursal: str):
    print("ejecutar mensaje")
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue=SUPPLY)
    message = "se necesita " + \
        str(count)+" unidades del producto con codigo " + \
        str(code)+" en la sucursal "+sucursal+"."
    channel.basic_publish(exchange='', routing_key=SUPPLY, body=message)
    print(f"sent mesagge: {message}")
    connection.close()
