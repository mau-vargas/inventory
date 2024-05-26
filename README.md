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


## How to update the image?

```bash
docker login

docker build src/ -t kanata333/fastapi-example:v<version tag>
docker buildx build -t inventory-fastapi:0.0.1 . #funciona

docker push kanata333/fastapi-example:v<version tag>
```


Levantar minikube:
minikube start

minikube dashboard


Instalar Argo: 
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


Exponer argoserver
kubectl port-forward svc/argocd-server -n argocd 8080:443


Obtener contraseña del usuario admin
kubectl -n argocd get pods -l app.kubernetes.io/name=argocd-server -o name | cut -d'/' -f 2

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo



Resultado: iJKpoS4aJOhAj6hC


crear la imagen
docker login

docker build src/ -t inventory-fastapi

docker push kanata333/fastapi-example:v<version tag>


docker push inventory-fastapi

---------------------
restablecer el codigo

git fetch origin                
git reset --hard origin/main
