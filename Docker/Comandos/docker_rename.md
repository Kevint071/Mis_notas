# Comando docker rename

        docker rename

Este comando le cambia el nombre a un contenedor. Este comando quita el nombre actual del contenedor y le agrega el que el usuario escriba.

## Formas de ejecutar este comando  

1. Por medio del nombre del contenedor

        docker rename <nombre_actual> <nombre_nuevo>
        
2. Por medio del ID del contenedor
        
        docker rename <id_contenedor> <nombre_nuevo>

>Esto no crea un nuevo contenedor como lo hacia el comando run. Este le cambia el nombre a el mismo contenedor.
