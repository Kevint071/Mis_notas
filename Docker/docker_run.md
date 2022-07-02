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

## Un ejemplo con el contenedor ubuntu:

        docker run ubuntu (corre un ubuntu pero lo deja apagado)
        docker run -it ubuntu (lo corre y entra al shell de ubuntu)

Para ver la version de linux (ubuntu) que estamos usando ingrese en la shell:

        cat /etc/lsb-release

Para salir de ubuntu, ingrese en la shell de ubuntu:

        exit

## Traer un contenedor al exterior por medio de un puerto

Ahora para traer un contenedor al exterior (contenedor nginx) usaremos el siguiente comando:

        docker run  --name proxy -d -p 5040:80 nginx

- proxy es el nombre nuevo que le asigne a este contenedor
- 5040 es el puerto de mi pc que decidi asignarle y 80 es el puerto del contenedor
- El puerto 5040 es variable mientras que el puerto 80 viene con el contenedor y no se puede modificar

Lo que se hizo en este comando fue cambiarle el nombre al contenedot nginx por el nombre "proxy" y se vinculo a nuestra computadora por medio del puerto 5040 con el puerto del contenedor el cual es el 80.

## Ver el puerto del contenedor:

        docker ps

## Dejar el contenedor "ubuntu" activo

Cuando se quiera dejar este contenedor activo o corriendo, aun así se  esté afuera del contenedor, se hace lo siguiente:

        docker run --name <nombre_nuevo> -d ubuntu tail -f /dev/null

>Si quieres puedes omitir el "--name <nombre_nuevo>"  

Con el comando anterior, se corre el archivo null y hasta que ese proceso no se detenga (que es el principal), el contenedor no se detendrá.

### Atributo -d

La funcion del atribudo -d es el de dejar activo un contenedor, ya que sin este, el contenedor se apagaría.