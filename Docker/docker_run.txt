El comando:

        docker run

se utiliza para ejecutar contenedores de Docker pero para correr un contenedor en específico se ejecuta con el nombre de la siguiente forma:

        docker run <contenedor>

Como función especial de docker run, este comando no ejecuta el mismo contenedor que ejecutó antes, sino que crea uno nuevo y lo ejecuta.

Si.. lindo y todo, pero no es la única función de este comando. Tambien puedes crear el mismo contenedor con otro nombre usando el atributo "--name (en resumen es como copiar un contenedor pero con otro nombre):

        docker run --name <nombre_nuevo> <nombre_imagen>

Esto hará que se cree un nuevo contenedor con otro nombre. Ojo que esto crea un nuevo contenedor, no le cambia el nombre al actual.

Algo que no se puede hacer es intentar crear 2 contenedores con el mismo nombre

Ahora para traer un contenedor al exterior (contenedor nginx) usaremos el siguiente comando:

        docker run  --name proxy -d -p 5040:80 nginx

Lo que se hizo en este comando fue cambiarle el nombre al contenedot nginx por el nombre "proxy" y se vinculo a nuestra computador por medio del puerto 5040 con el puerto del contenedor el cual es el 80.

Para ver el puerto del contenedor se ejecuta el comando:

        docker ps