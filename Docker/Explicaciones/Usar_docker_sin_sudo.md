Para usar Docker sin tener que usar a cada rato el comando "sudo" hay que hacer lo siguiente: 

1.  Creas un grupo Docker:
        
        sudo groupadd docker
    
2.  Agregas tu usario en el grupo Docker (Para conocer tu usario en la terminal Bash ejecuta el comando whoami):

        sudo usermod -aG docker $USER
    
>Reemplaza $USER por tu usuario

3. Cierra la sesión y ya habrás terminado

4. Para no utilizar sudo, hay que activar el grupo creado con el comando:

        newgrp docker

5. Para verificar si no hay errores ejecute el siguiente contenedor de prueba:

        docker run hello-world

> Si al ejecutar el contenedor, te sale un mensaje de bienvenida, ya puedes usar Docker