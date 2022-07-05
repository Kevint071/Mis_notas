# Almacenando un contenedor dentro de un volumen

## 1. Crear volumen

Para crear un volumen se usa el comando:

    docker volume create <nombre>

## 2. Montar un contenedor dentro del volumen

Ahora montamos un contenedor dentro de un volumen (en este caso, el contenedor mongo):

    docker run -d --name db --mount src=dbdata,dst=/data/db mongo

- -d (deatch) sirve para poner contenedores corriendo en segundo plano
- --mount monta el contenedor en el volumen
- src (source) especifíca el nombre del volumen
- dst (destino) sirve para la direccion donde el contenedor va a estar montado

## 3. Ejecutar el contenedor

Para hacerlo escribimos el siguiente comando:

    docker exec -it db bash

Listo, se nos debería abrir el bash de este contenedor. Si queremos usar mongo, escribimos el comando:

    mongo

> Lo que guardemos dentro de este volumen, quedará allí, aún si eliminamos el contenedor