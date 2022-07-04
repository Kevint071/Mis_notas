# Usando el contenedor "ubuntu"

## Ejecutar el contenedor "ubuntu"

        docker run ubuntu (corre un ubuntu pero lo deja apagado)
        docker run -it ubuntu (lo corre y entra al shell de ubuntu)

Para ver la version de linux (ubuntu) que estamos usando ingrese en la shell:

        cat /etc/lsb-release

Para salir de ubuntu, ingrese en la shell de ubuntu:

        exit

## Dejar el contenedor "ubuntu" activo

Cuando se quiera dejar este contenedor activo o corriendo, aun así se  esté afuera del contenedor, se hace lo siguiente:

        docker run --name <nombre_nuevo> -d ubuntu tail -f /dev/null

>Si quieres puedes omitir el "--name <nombre_nuevo>"   pero esto generará un nombre aleatorio para el contenedor. Es tu desicion...

Con el comando anterior, se corre el archivo null y hasta que ese proceso no se detenga (que es el principal), el contenedor no se detendrá.

### Atributo -d

La funcion del atribudo -d es el de dejar activo un contenedor, ya que sin este, el contenedor se apagaría. En otras palabras deja el contenedor corriendo en segundo plano.