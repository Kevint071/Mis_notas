# Comando "apt-get update" ó "apt update"

Este comando usualmente sirve para mostrar las actualizaciones que se deben hacer en el sistema, pero aveces muestra que hay varios paquetes que están configurados varias veces.<br><br>

## 1. Abrir software y actualizaciones

Para abrir esta app, ejecutamos el siguiente comando:

    sudo software-properties-gtk

<br> Ahora se nos abrirá la ventana de software y aplicaciones:

<img width=700 src="../Imagenes/Ubuntu_software.png"/> <br>

## 2. Usando la aplicación

1. Nos dirigimos a la seccion de **Otro software**:

    <img width=400 src="../Imagenes/Otro_software_1.png"/> <br>

2. Desmarcamos las casillas que esten seleccionadas:

    <img width=500 src="../Imagenes/Otro_software_2.png"/> <br>

3. Presionamos el boton cerrar:

    <img width=700 src="../Imagenes/Otro_software_3.png"/> <br>

4. Ahora presionamos en el botón recargar:

    <img width=500 src="../Imagenes/Recargar_1.png"/> <br>

Listo, ya con esto terminariamos el proceso. La ventana de actualizaciones debería cerrarse.

## 3. En caso de errores:

<br>En caso de que nos salga este error cuando usemos el botón recargar:

<img width=500 src="../Imagenes/Fallo.png"/> <br>

- Ejecutamos el siguiente comando:

        sudo rm /etc/apt/sources.list

- Si nos arroja un error es porque ese archivo ya no existe. Ahora ejecutamos el siguiente comando:

        sudo rm /etc/apt/sources.list.d/* -vf

- Ya con esto procedemos a repetir el comando:

        sudo software-properties-gtk

- Seleccionamos las primeras 4 casillas de ubuntu-software:

    <img width=700 src="../Imagenes/Ubuntu_software.png"/> <br>

- Presionamos el botón cerrar:

    <img width=500 src="../Imagenes/Ubuntu_software_2.png"/> <br>

- Por último presionamos el botón revertir y cuando termine de ejecutarse, ejecutamos en la terminal:

        sudo apt-get update

Ya veremos que no está mas ese error.
