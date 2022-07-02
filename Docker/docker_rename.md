Con el comando

        - docker rename

Se le cambia el nombre a un contenedor. Este comando quita el nombre viejo del contenedor y le agrega el que el usuario escriba.

Para hacer esto se ejecuta el comando de la siguiente forma:

        1. docker rename nombre_actual nombre_nuevo
        2. docker rename id_del_contenedor nombre_nuevo

Esto no crea un nuevo contenedor como lo hacia el comando run. Este le cambia el nombre a el mismo contenedor.
