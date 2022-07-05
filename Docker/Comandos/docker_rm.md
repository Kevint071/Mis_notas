# Comando docker rm

        docker rm

Con este comando se puede eliminar un contenedor de la lista de contenedores que tengamos en nuestro sistema.

## Maneras de ejecutarlo

1. Por el nombre del contenedor

        docker rm <nombre_contenedor>

2. Por el id del contenedor

        docker rm <id_contenedor>

## Atributo -f
    
Para borrar definitivamente un contenedor se usa el atributo "-f". Esto es por si sucede algun inconveniente en el borrado.

        docker rm -f <nombre_contenedor>
        docker rm -f <id_contenedor>

## Usando docker --rm

Este comando se utiliza cuando vaya a eliminar un contenedor después de ejecutarlo:

        docker run --rm <contenedor>