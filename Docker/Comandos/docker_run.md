# Comando docker run

        docker run

Se utiliza para ejecutar contenedores de Docker pero para correr un contenedor en específico se ejecuta con el nombre de la siguiente forma:

        docker run <contenedor>

Como función especial de docker run, este comando no ejecuta el mismo contenedor que ejecutó antes, sino que crea uno nuevo y lo ejecuta.

## Crear el mismo contenedor con otro nombre

Tambien puedes crear el mismo contenedor con otro nombre usando el atributo "--name" (en resumen es como copiar un contenedor pero con otro nombre)

        docker run --name <nombre_nuevo> <nombre_imagen>

Esto hará que se cree un nuevo contenedor con otro nombre. 
- Ojo que esto crea un nuevo contenedor, no le cambia el nombre al actual.
- Algo que no se puede hacer es intentar crear 2 contenedores con el mismo nombre

## Atributo -it

        docker run -it nombre_contenedor 

Se puede interactuar con el contenedor si este tiene entrada.

## Las funciones i y t en "-it" son:

        i: interactivo
        t: abre la consola

## Atributo -p

Este atributo sirve para publicar un contenedor y poderlo conectar a un puerto

        docker run -p -d <puerto_maquina>:<puerto_contenedor> <nombre_contenedor>