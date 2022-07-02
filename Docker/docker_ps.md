# Comando docker ps

        - docker ps

Con este comando, se muestran los contenedores que estén activos pero no muestra todos los contenedores.

## Atributo -a

Con este atributo muestran tanto los contenedores que estén activos como los que no

        - docker ps -a

Una muestra de este comando con el contenedor de hello-world

        CONTAINER ID      IMAGE                            COMMAND                      CREATED                                    STATUS                                            PORTS                           NAMES
        d1834f844143         hello-world               "/hello"                         12 seconds ago                Exited (0) 8 seconds ago                                                         adoring_spence