El comando

        - docker rm

Puede eliminar un contenedor de la lista de contenedores que tengamos en nuestro sistema de la siguientes formas:

        1. docker rm <contenedor>
        2. docker rm <id_contenedor>
    
Para borrar definitivamente un contenedor se usa el atributo "-f". Esto es por si sucede algun inconveniente en el borrado.

        - docker rm -f <contenedor>