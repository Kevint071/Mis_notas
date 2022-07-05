# Usando el contenedor **ubuntu**

## Ejecutar el contenedor **ubuntu**

        docker run ubuntu (corre un ubuntu pero lo deja apagado)
        docker run -it ubuntu (lo corre y entra al shell de ubuntu)

Para ver la version de linux (ubuntu) que estamos usando ingrese en la shell:

        cat /etc/lsb-release

Para salir de ubuntu, ingrese en la shell de ubuntu:

        exit

## Dejar el contenedor **ubuntu** activo

Cuando se quiera dejar este contenedor activo o corriendo, aun así se  esté afuera del contenedor, se hace lo siguiente:

        docker run --name <nombre_nuevo> -d ubuntu tail -f /dev/null

>Si quieres puedes omitir el "--name <nombre_nuevo>"   pero esto generará un nombre aleatorio para el contenedor. Es tu desicion...

Con el comando anterior, se corre el archivo null y hasta que ese proceso no se detenga (que es el principal), el contenedor no se detendrá.

### Atributo -d

La funcion del atribudo -d es el de dejar activo un contenedor, ya que sin este, el contenedor se apagaría. En otras palabras deja el contenedor corriendo en segundo plano.

## Crear y públicar una imagen en base a la imagen **ubuntu**

## 1. Crear archivo Dockerfile

Se crea un archivo con el nombre "Dockerfile" en una carpeta donde vayas a crear la imagen.

>Recomendación: Crear una carpeta para este proceso o hacer esto donde este tu proyecto.

Ejemplo de Dockerfile:

        FROM ubuntu:latest

        RUN  touch /usr/src/hola.txt

- "ubuntu:lates" significa la última versión de la imagen **ubuntu**. 
- Para especificar una versión, por ejemplo la 18.04 se escribe "ubuntu:18.04"

## 2. Crear imagen en base al Dockerfile

> Es importante que se encuentre el dockerfile en el mismo lugar donde ejecutará este comando

Para este paso usaremos el comando "docker build" con el contenedor ubuntu:

        docker build -t ubuntu:mi_imagen .

## 3. Ingresar el usuario de DockerHub

Necesitamos ingresar nuestro usuario para poder agregar nuestra imagen a nuestro repositorio, así que ejeutamos el comando:

        docker login

Ahora ingresamos nuestro usuario o ID y nuestra contraseña. Si queremos cerrar sesión ejecutamos el comando:

        docker logout

## 4. Añadir nuestro nombre al repositorio

Pero observamos la imagen que copiamos de ubuntu con nuestros archivos sigue con el repositorio de **ubuntu**:

        REPOSITORY         TAG         IMAGE ID       CREATED        SIZE
        ubuntu             mi_imagen   80a383d5402c   2 hours ago    77.8MB
        ubuntu             latest      27941809078c   4 weeks ago    77.8MB

Para cambiar esto, ejecutamos el siguiente comando:

        docker tag ubuntu:mi_imagen usuario_DockerHub/ubuntu:mi_imagen

- En mi caso, usare mi usuario pero ustedes usen el suyo.

Ahora si ejecutamos "docker ls" veremos:

        REPOSITORY         TAG         IMAGE ID       CREATED        SIZE
        ubuntu             mi_imagen   80a383d5402c   2 hours ago    77.8MB
        kevint0/ubuntu     mi_imagen   80a383d5402c   2 hours ago    77.8MB
        ubuntu             latest      27941809078c   4 weeks ago    77.8MB

## 5. Publicar repositorio

Para publicar el repositorio ejecutamos el comando:

        docker push kevint0/ubuntu:mi_imagen

Ahora pueden revisar en su cuenta de DockerHub su repositorio
