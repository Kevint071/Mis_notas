# Mostrar sistemas operativos ocultos en GRUB

Aveces cuando queremos entrar a un sistema operativo específico, en el GRUB, no se nos muestra al iniciar nuestro ordenador. Así que para hacer que aparezca en el GRUB es hacer lo siguiente (en un SO linux):

<br>

## 1. Entrar en el directorio GRUB

Para entrar en este archivo de texto, lo localizamos en el directorio /etc/default/grub, pero abriremos este archivo mas tarde. Por ahora solo entremos en el directorio de la carpeta default.

<br>

## 2. Cambiar permisos del archivo

Aveces encontramos problemas al editar este archivo ya que nos puede decir que es de solo lectura, por lo que abrimos una terminal dentro de la carpeta **default** y ejecutamos el siguiente comando:

<br>

    sudo chmod a+rw grub

<br>

Con este comando editamos los permisos del archivo **grub** para que podamos editarlo sin ningun inconveniente.

<br>

## 3. Abrir el archvo de texto GRUB

Cuando abramos este archivo agregamos lo siguiente:

<br>

    GRUB_DISABLE_OS_PROBER=false

<br>

## 4. Actualizar el GRUB

Para que aparezcan los sistemas operativos ejecutamos dentro de una terminal el siguiente comando:

<br>

    sudo update-grub

<br>

Ya con estos pasos solo queda reiniciar el ordenador y ya te deberían aparecer los demas sistemas operativos o SO que tienes instalados.

<br>

Si algo les sale mal en este proceso me pueden escirbir al correo andrestorrecilla.14@gmail.com