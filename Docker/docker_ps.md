# Comando docker ps

        docker ps

Con este comando, se muestran los contenedores que estén activos pero no muestra todos los contenedores.

## Atributo -a

Con este atributo muestran tanto los contenedores que estén activos como los que no

        docker ps -a

Una muestra de este comando con el contenedor de hello-world

        CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
        3ba3af62bdd0   hello-world   "/hello"   5 seconds ago   Exited (0) 3 seconds ago             serene_taussig
