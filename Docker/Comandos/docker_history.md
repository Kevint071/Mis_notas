# Comando docker history

Este comando sirve para mostrar las capas de los contenedores:

    docker history <imagen>

## Ejemplo con el contenedor de **ubuntu**

Se ejecuta el comando history de la siguiente manera:

    docker history ubuntu

Ahora la terminal arrojará lo siguiente:

    IMAGE          CREATED       CREATED BY                                      SIZE      COMMENT
    27941809078c   4 weeks ago   /bin/sh -c #(nop)  CMD ["bash"]                 0B        
    <missing>      4 weeks ago   /bin/sh -c #(nop) ADD file:11157b07dde10107f…   77.8MB    
