# Descartar cambios con git reset

Para descartar cambios del ultimo **commit** y volver al **commit** que se tenía anteriormente, sea por que ya tu código ha dejado de funcionar o por otros motivos inesperados, se usa el comando:

       git reset --hard HEAD~1

Eso funciona para volver un commit atras, borrando el ultimo commit o descartando los últimos cambios que se han hecho si no se ha guardado un commit.

>Si se coloca un número despues del "~" (por ejemplo un 2), te lleva al **penúltimo commit** y así sucesivamente (si colocas un 3 te lleva al antepenúltimo commit borrando los otros 2).

Hay que tener cuidado cuando se vaya a usar este comando, sobretodo si se han creado nuevos archivos, porque al hacer esto, estás dejando tu trabajo hecho hasta el penúltimo commit que hiciste (el commit antes del commit no deseado), por lo que si creaste un archivo despues del penúltimo commit que guardaste , perderás el progreso hecho.