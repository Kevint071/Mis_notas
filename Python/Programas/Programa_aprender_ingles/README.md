# Como usar esta base de datos para aprender vocabulario de ingles

## 1. Crea una cuenta en railway

Este programa usa una conexión de base de datos con railway, asi que debes crearte una cuenta y luego crea un nuevo proyecto de tipo base de datos con postgresql.

<br>

## 2. Crea una tabla

Copia el contenido del archivo **db.sql** y luego pegalo en el query de railway en la tabla de postgresql ya creada en el paso 1.

<br>

## 3. Conecta la tabla con el archivo **Aprender_palabras.py**

        def credenciales():
            link_db = "link coneccion"
            return link_db

<br>

## 3. Ejecutar programa

Ahora ejecuta el programa **Aprender_palabras.py**

