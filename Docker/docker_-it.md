# Comando docker run

        - docker run -it nombre_contenedor 

Se puede interactuar con el contenedor si este tiene entrada.

Un ejemplo es con ubuntu:

        - docker run ubuntu (corre un ubuntu pero lo deja apagado)
        - docker run -it ubuntu (lo corre y entro al shell de ubuntu)

Las funciones i y t en "-it" son:

-i: interactivo
-t: abre la consola

Para ver la version de linux (ubuntu) que estamos usando ingrese en la shell:

        - cat /etc/lsb-release (veo la versión de Linux)

Para salir de ubuntu, ingrese en la shell de ubuntu:

        - exit


Cuando se quiera dejar el contenedor activo aun así se salga del contenedor se hace lo siguiente:

        - docker run --name nombre_nuevo -d ubuntu tail -f /dev/null

ubuntu lo puedes reemplazar por el nombre actual de tu contenedor

Con elcomando anterior, se corre el proceso de null que es un archivo y hasta que ese proceso no se detenga, que es el principal, el contenedor no se detendrá.