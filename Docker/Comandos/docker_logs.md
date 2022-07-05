# Comando docker logs

        docker logs

Con este comando, puedes mirar los cambios que se den dentro de un contenedor mientras este esté activo.

        docker logs <contenedor>

## Atributo -f

Para mirar los cambios que sucedan en tiempo real, se ejecuta el comando anterior con el atributo "-f"

        docker logs -f <contenedor>

Para mirar los cambios en tiempo real pero los últimos 10 cambios que se han  hecho, se ejecuta el siguiente comando: 

        docker logs tail 10 -f <contenedor>

>Puedes cambiarle el número 10 por el que quieras

