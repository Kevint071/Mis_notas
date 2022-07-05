# Comando docker build

El comando build sirve para construir una imagen en base a un **Dockerfile**, con el comando.

    docker build -t  <imagen_base>:<nombre_tag> <contexto_dockerfile>

- El <contexto_dockerfile> es un directorio y por lo general, en desarrollo, siempre se coloca un punto (.), ya que este directorio hace referencia a la carpeta actual.

Ahora para ver la imagen creada se ejecuta el comando:

    docker image ls

## Atributo -t

El atributo **-t** con el comandodo **build** sirve para asignarle el nombre a la imagen.

