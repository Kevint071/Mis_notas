# Comando docker cp
Este comando puede copiar un archivo a un contenedor o extraer un archivo del contenedor y copiarlo en algun directorio.

    docker cp

## Insertar archivo en un contenedor

- Recuerda que debes estar en el directorio donde están los archivos que quieres copiar al contenedor
- Haremos este ejemplo con el contenedor de ubuntu.

    >Debes tener el contenedor de ubuntu activo, para hacer esto mira el archivo de este mismo repositorio <a href="../Contenedores/Contenedor_ubuntu.md">**Contenedor_ubuntu.md**</a>

<br>

Una vez el contenedor esté activo y estemos en el repositorio donde vamos a compartir nuestro archivo o carpeta, ejecutamos el siguiente comando:

    docker cp <archivo_carpeta> <nombre_contenedor>:/directorio/<cambiar_nombre_archivo_o_carpeta>

<br>

Si usamos este comando en ubuntu:

    docker run --name mi_ubun -d ubuntu tail -f /dev/null

- El nombre **mi_ubun** es el nombre que le puse al contenedor **ubuntu** <br><br>

Y dentro de el contenedor **ubuntu** creamos una carpeta llamada "archivos", el comando **cp** quedaría:

    docker cp mi_archivo.txt mi_ubun:/archivos/archivo_in_ubuntu.txt

- **archivo_in_ubuntu.txt** es el nuevo nombre que le asigne a **mi_archivo.txt**
- Es opcional cambiarle el nombre al archivo o a la carpeta que se quiera copiar. Si no quieres cambiarselo, deja solamente el directorio.

<br>

## Extraer un archivo de un contenedor

<br>

Ahora para extraer este archivo vamos a posicionarnos en la terminal en el directorio que queremos que se nos copie el archivo.

Ahora si queremos extraer el archivo anterior **archivo_in_ubuntu.txt** hacemos lo siguiente:

    docker cp mi_ubun:/test/archivo_in_ubuntu.txt archivo_extraido.txt

- **archivo_extraido.txt** es el mismo archivo que **archivo_in_ubuntu** sino que con otro nombre. En este caso el nombre si es obligatorio, pero puede ser el mismo que está en el contenedor