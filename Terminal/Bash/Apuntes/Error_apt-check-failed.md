# Errores de apt-check failed

Cuando se actualizan los paquetes de ubuntu al final suele salir que hay un error que nos dice que esta fallido apt-check. Entonces para eso escribimos el siguiente comando:<br><br>

    sudo dpkg-reconfigure libdvd-pkg
<br>

>Esto lo que hace es que va a reconfigurar los paquetes para que la proxima vez que los actualicemos o instalemos se haga el proceso sin este anuncio de error.