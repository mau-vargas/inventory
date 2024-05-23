# Inventario
Proyecto para administrar un inventario




## Herramientas utilizadas:
<table style="border-collapse: collapse; background-color: transparent;">
  <tr>
    <td><img src="https://github.com/mau-vargas/inventory/blob/main/image/Python.png" alt="Logo de Python" width="50"/></td>
    <td><img src="https://github.com/mau-vargas/inventory/blob/main/image/FastAPI.png" alt="Logo de FastAPI" width="50"/></td>
    <td><img src="https://github.com/mau-vargas/inventory/blob/main/image/RabbitMQ.png" alt="Logo de RabbitMQ" width="50"/></td>
    <td><img src="https://github.com/mau-vargas/inventory/blob/main/image/postgreSQL.png" alt="Logo de PostgreSQL" width="50"/></td>
    <td><img src="https://github.com/mau-vargas/inventory/blob/main/image/dbschema.jpeg" alt="Logo de DbSchema" width="50"/></td>
    <td><img src="https://github.com/mau-vargas/inventory/blob/main/image/docker.png" alt="Logo de Docker" width="50"/></td>
  </tr>
</table>

- Python : **3.11.3** 
- FastApi : https://fastapi.tiangolo.com/
- RabbitMQ : https://www.rabbitmq.com/
- PostgreSQL : https://www.postgresql.org/
- DBSchema : https://dbschema.com/index_es.html
- Docker : https://www.docker.com/

# Inicar el proyecto

## FastApi
fastapi dev app/main.py

## Iniciar docker:
- docker-compose up
- Se levantará RabbitMQ y PostgreSQL.

## Para abrir la ui de rabbit
- http://localhost:15672/

## PostgreSQL
- http://localhost:5432

## DbSchema
- HOST=http://localhost:5432
- POSTGRES_PASSWORD=admin_password
- POSTGRES_USER=admin_user
- POSTGRES_DB=inventory_db


## Docker
#listar docker
#docker ps 

#Seleccionar un docker para entrar a la consola
#docker exec -i -t 05eeba6aa75e /bin/bash 

#PostgreSQL
#listar tablas
#\dt

#listado de productos
SELECT * FROM inventory;
