# Usando contenedor de platzi

Crear una red con el siguiente comando:

    docker network create platzinet

<br>

Correr el siguiente contenedor:

    docker run -d --name db mongo

<br>

Conectar el contenedor de mongo creado con la red **platzinet**:

    docker network connect platzinet db

<br>

Ahora le asignamos el puerto al que se va a conectar el contenedor de platzi:

    docker run -d --name app -p 3000:3000 --env MONGO_URL=mongodb://db:27017/test platziapp

<br>

Conectamos el contenedor **platziapp** a la red platzinet:

    docker network connect platzinet app

<br>

Ya con esto el contenedor de platzi estaría funcionando ya que le conectamos el contenedor de mongo por medio de un puerto (3000) a una misma red.

<br>

## Usar docker-compose

<br>

Para hacer todo esto sin necesidad de todo lo anterios, nos ubicamos en la terminal donde está el archivo **docker-compose.yml** ejecutamos el siguiente comando:

    docker-compose up

Esto hará lo mismo y mucho mas facil.  

<br>

Para ejecutar este proceso en segundo plano se utiliza el comando:  

    docker-compose up -d

## Hacer un cambio en index y subirlo en compose

Para hacer un cambio en index.js y trabajar con docker-compose nos aseguramos que el Dockerfile esté así:

<br>

<img width=500 src="../../../Imagenes/Dockerfile.png">

<br>

Ahora, el archivo **docker-compose.yml** tiene que estar así.

<br>

<img width=400 src="../../../Imagenes/docker-compose.yml.png">

<br>