# Activar y desactivar base atras del comando de terminal 


Por lo general cuando se instala Anaconda, aparece en nuestra terminal algo parecido despues de instalarla:

<br>

<img src="Imagenes/Base.png" width=550 height=350>

<br>

Entonces para quitar esa palabra **(base)** se ejecutan los siguientes pasos:

<br>

## 1. Se comprueba si "*auto_activate_base*" esta como activado

<br>

Esto se puede lograr con el siguiente comando:

<br>

    conda config --show | grep auto_activate_base

<br>

Este comando dirá True o False dependiendo si está activado o no.

<br>

## 2. Desactivar ese comando

<br>

Para hacer esto se ejecuta el siguiente comando:

<br>

    conda config --set auto_activate_base False

Ya con esto se quitará esta palabra de la terminal.

<br>

## 3. Activar ese comando

<br>

Sin este comando no se podrá iniciar el ambiente conda y por lo tanto no podrás ejecutar comandos de **Anaconda**. Para activarlo se ejecuta el siguiente comando:

<br>

    conda config --set auto_activate_base True

<br>

Para ver si funciona realmente este comando ejecuten el siguiente comando con el auto_activate_base en True y en False:

<br>

    jupyter notebook

