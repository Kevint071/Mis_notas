# Mostrar y ocultar la barra de actividades de VS Code

Para hacer esto tenemos que abrir el archivo local settings.json y si no tienes uno, se creará automaticamente.

<br />

Para hacerlo ejecutamos el siguiente comando:

    ctrl + shift + p

Ahora escribimos lo siguiente:

    Workspace Settings JSON

Cuando ejecutemos esto se nos abrirá el archivo de opciones json. Ahora agregamos el siguiente codigo:

    {
      "workbench.activityBar.visible": false,
    },

Y ya no nos aparecerá la barra de actividades, si queremos volverla a mostrar cambiamos el valor **false** a **true**

    {
      "workbench.activityBar.visible": true,
    },

<br/><br/>

# Mostrar y ocultar la barra de actividades de VS Code

Ahora simplemente para hacer esto agregamos esta linea al mismo archivo:

    "workbench.statusBar.visible": false,

Y quedaria de la siguiente manera

    {
      "workbench.activityBar.visible": false,
      "workbench.statusBar.visible": false,
    },

