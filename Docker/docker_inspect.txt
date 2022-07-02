La funcion del comando

        - docker inspect #

es mostrar a detalle un contenedor específico. Hay 2 maneras de poder seleccionarlo las cuales son:

1. Por medio del ID del contenedor:

        En este caso usamos el comando:

        - docker inspect ID

        Reemplazando la palabra ID por el ID del contenedor que se quiera usar

2. Por medio del nombre del contenedor:

        Es como el caso anterior pero se usa:

        - docker inspect NAME

        Reemplazando NAME por el nombre del contenedor


Para obtener el ID del proceso principal de un contenedor se ejecuta el comando:

                - docker inspect --format '{{.State.Pid}}' nombre_contenedor

Para matar el proceso principal se ejecuta el comando:

                - kill -9 ID