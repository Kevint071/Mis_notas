# Comando docker inspect

        docker inspect #

Este comando, muestra a detalle un contenedor específico.

## Maneras de ejecutar el comando docker inspect

1. Por medio del ID del contenedor:

        docker inspect ID

        Reemplazando la palabra ID por el ID del contenedor que se quiera usar

2. Por medio del nombre del contenedor:
        
        Es como el caso anterior pero se usa:

        docker inspect NAME
        
        Reemplazando NAME por el nombre del contenedor


## Obtener ID del proceso principal del contenedor

Por lo general se usa este comando cuando se quiere matar el proceso de un contenedor

                docker inspect --format '{{.State.Pid}}' nombre_contenedor

Para matar el proceso principal se ejecuta el comando:

                kill -9 ID