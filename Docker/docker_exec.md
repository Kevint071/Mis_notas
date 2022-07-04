# Comando docker exec

    docker exec

Este comando sirve para ejecutar un contenedor. Este comando recibe 3 parámetros, de los cuales 1 son opcionales y 2 parámetros son obligatorios.

    docker exec <opciones> <nombre_contenedor> <argumentos>

## Ejemplo con el contenedor de ubuntu

- Primero ponemos a correr el contenedor de ubuntu, ya que si no está activo, no funcionaría

        docker run --name nombre_random -d ubuntu tail -f /dev/null

- Para comprobar que el contenedor esté activo escribimos el siguiente comando:

        docker ps

- Debería salir esto:

        CONTAINER ID   IMAGE     COMMAND               CREATED         STATUS         PORTS     NAMES
        af8f03313d54   ubuntu    "tail -f /dev/null"   5 seconds ago   Up 3 seconds             nombre_random

- Ahora que ya hemos comprobado que está activo, procedemos a ejecutar el bash

        docker exec -it nombre_random bash

- Ya se nos debería abrir la terminal bash de linux
