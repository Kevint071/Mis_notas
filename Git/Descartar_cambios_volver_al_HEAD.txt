Para descartar cambios del ultimo commit y volver al commit que se tenia anteriormente, sea por que ya tu código ha dejado de funcionar o por otros motivos inesperados se usa el comando:

       git reset --hard HEAD~1

Eso funciona para volver un commit atras borrando el ultimo commit o descartando los últimos cambios que se han hecho si no se ha guardado un commit.

Si se coloca un número despues del "~" despues del guion curvado (por ejemplo un 2), te lleva al penultimo commit y asi sucesivamente (si colocas un 3 te lleva al antepenultimo commit borrando los otros 2).

Hay que tener cuidado cuando se vaya a usar, sobretodo si se han creado nuevos archivos porque al hacer esto, estás dejando tu trabajo hecho hasta el ultimo commit que hiciste(el commit antes del no deseado), por lo que si creaste un archivo despues del ultimo commit que guardaste (el commit antes del no deseado), perderás el progreso hecho.