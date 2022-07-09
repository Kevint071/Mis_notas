# Crear una usb booteable

Por lo general se crean usb booteables para instalar sistemas operativos desde una memoria y en algunos casos, el proceso de convertir una usb a una booteable puede dar problemas si se usan aplicaciones de terceros como rufus.

Lo bueno es que hay una forma de poder crear usb booteables desde la terminal de linux, no importa que distribución uses.

<br>

## 1. Estar en modo root o administrador

<br>

Para hacer esto usamos el comando:

    sudo -s

Luego ingresamos nuestra contraseña de usuario y listo.

<br>

## 2. Listar los dispositivos y particiones

<br>

Este comando lo usamos para ver las particiones hechas y nuestro pendrive:

    fdisk -l

Por lo general nuestra memoria siempre usará el disco /dev/sdb

    Disco /dev/sdb: 7,51 GiB, 8053063680 bytes, 15728640 sectores
    Disk model: Flash Disk      
    Unidades: sectores de 1 * 512 = 512 bytes
    Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
    Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
    Tipo de etiqueta de disco: dos
    Identificador del disco: 0x00000000

<br>

## 3. Desmontar el dispositivo usb

<br>

Para desmontar el pen drive hacemos lo siguiente:

    umont /dev/sdb1

En caso de que les salga el error **"umount: /dev/sdb1: no montado."**, escriban el siguiente comando:

    umont /dev/sdb

<br>

## 4. Formateamos la usb a un formato FAT

<br>

Con el comando a continuación, formatearemos el usb a un formato **FAT** y con el atributo **-F** definiremos el tipo de formato. Lo mas recomendable es usar el formato **FAT 32**:

    mkfs.vfat -F 32 /dev/sdb -I

Formatear en formato **FAT 16**:

    mkfs.vfat -F 16 /dev/sdb -I

## 5. Hacemos el proceso para tener la usb booteable

<br>

Para convertir la usb a booteable, ejecutamos el siguiente comando: 

    dd if=imagen_iso of=/dev/sdb

> La imagen iso ya debe estar descargada

Si quieres ver el progreso del proceso, instala el paquete **pv**:

    apt-get install pv

Ahora ejecutamos el comando:

    dd if=imagen_iso |pv| dd of=/dev/sdb