# Usando el contenedor "nginx"

## Ejecutar el contenedor "nginx"

Ejecutamos este contenedor con el comando:

    docker run --name proxy  nginx

Si quieres que "nginx" quede activo usa el atributo "-d" para correr el contenedor en segundo plano:

    docker run --name proxy -d nginx

## Ver el puerto de "nginx"

Ya se sabe que el puerto por defecto de nginx es el 80 pero por si quieres saber como mirar el puerto, luego de ejecutar el comando anterior, escribimos en la terminal:

    docker ps

Debería mostrar el puerto en la columna **PUERTOS**

    CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
    ee13bc56ef94   nginx     "/docker-entrypoint.…"   4 seconds ago   Up 2 seconds   80/tcp    proxy

## Traer el contenedor "nginx" al exterior por medio de un puerto

>Primero borra el contenedor de nginx anterior

Ahora, para traer el contenedor **nginx** al exterior, usaremos el siguiente comando:

        docker run  --name proxy -d -p 5040:80 nginx

- proxy es el nombre nuevo que le asigne a este contenedor
- 5040 es el puerto de mi pc que decidi asignarle y 80 es el puerto del contenedor
- El puerto 5040 es variable mientras que el puerto 80 viene con el contenedor y no se puede modificar

Lo que se hizo en este comando fue cambiarle el nombre al contenedot nginx por el nombre **proxy** y vincular el contenedor a nuestra computadora por medio del puerto 5040 con el puerto del contenedor el cual es el 80.

## Ver la conexión de puertos:

Se ejecuta este comando:

    docker ps

Debería mostrar la conexión hecha entre los 2 puertos  en la columna **PUERTOS**

    CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
    24bbce79353d   nginx     "/docker-entrypoint.…"   10 seconds ago   Up 3 seconds   0.0.0.0:5000->80/tcp, :::5000->80/tcp   proxy