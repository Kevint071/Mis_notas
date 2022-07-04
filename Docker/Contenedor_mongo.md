# Usando contenedor mongo

## Ejecutar el contenedor

Para ejecutar el contenedor **mongo** , escribimos el siguiente comando:

    docker run --name db mongo

>Puedes omitir el "--name db" pero es una buena práctica ponerle nombres a los contenedores

## Activar en segundo plano el contenedor "mongo"

Para ejecutar el contenedor **mongo** en segundo plano, escribimos el siguiente comando:

    docker run -d --name db mongo

## Ejecutar el contenedor activo

>Para hacerlo, el contenedor debe estar activado (corriendo en segundo plano). 

Para ejecutar el contenedor, escribimos el siguiente comando:

    docker exec -it db bash

Listo, se debería abrir el bash de este contenedor. Si queremos usar mongo, escribimos el comando:

    mongo

# Funciones de mongo

## use

El comando **use** se utiliza para crear un usuario:

    use <nombre_usuario>

## db.users.insert()

Este comando se usa para insertar datos dentro del usuario:

    db.users.insert({"nombre": "tu_nombre"})

>db es el nombre que estoy usando, pero tu puedes asignarle el que quieras con --name

## db.users.find()

Este comando se usa luego de crear un usuario con **use <nombre_usuario>** y sirve para ver los datos dentro del usuario en el que estemos:

    db.users.find()