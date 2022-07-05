# Comando docker-compose

Sirve para ejecutar varios contenedores de Docker y entrelazarlos

## Atributo up

Este atributo sirve para crear y comenzar los contenedores.

Para hacer esto nos ubicamos en la terminal, en el directorio donde este el archivo **docker-compose.yml** y ejecutamos el comando:

    docker-compose up

### Atributo -d

Para dejar este proceso corriendo en segundo plano ejecutamos el comando:

    docker-compose up -d

En este proceso los contenedores quedarán activos.

<br>

## Subcomandos de docker-compose

<br>

- Ver todos los logs de docker-compose

        docker-compose logs

- Ver los logs de un contenedor en compose

        docker-compose logs <nombre_contenedor>

- Ver los logs en tiempo real de un contenedor

        docker-compose logs -f <nombre_contenedor>

- Acceder al bash de un contenedor

        docker-compose exec <nombre_contenedor> bash

- Destruir los contenedores y la red de docker-compose

        docker-compose down