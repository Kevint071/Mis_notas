# Comando docker network

Este comando sirve para tratar con redes:

    docker network

## Listar las redes

Para hacer esto se usa el comando:

    docker network ls

Por lo general, docker tiene estas redes por defecto:

    NETWORK ID     NAME        DRIVER    SCOPE
    a34de077609f   bridge      bridge    local
    dbb22c0d40bc   host        host      local
    ee77ab0b8e90   none        null      local


## Crear una red

Esto se puede hacer con el comando:

    docker network create <nombre_red>

>Para ver la red que creaste, usa el comando de listar redes.

### Atributo --attachable

Este atributo sirve para permitir que otros contenedores se conecten a esta red:

    docker network create --attachable <nombre_red>

## Inspeccionar una red

El comando para inspeccionar una red de docker es el siguiente:

    docker network inspect <nombre_red>

## Conectar un contenedor a una red

Esto se hace con el comando:

    docker network connect <nombre_red> <nombre_contenedor>