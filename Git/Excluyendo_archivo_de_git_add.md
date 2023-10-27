# Excluir archivo de git al agregarlo con *add*

Para excluir a un archivo después de agregarlo con git add se hace lo siguiente:

    git rm --cached archivo.txt

>Con este comando, el archivo estará como si no se hubiera agregado con git add

Tambien se puede hacer con:

    git restore --staged archivo.txt

>Con este comando se hace lo mismo pero lo deja mejor sincronizado con git (es mas recomendable usar este)