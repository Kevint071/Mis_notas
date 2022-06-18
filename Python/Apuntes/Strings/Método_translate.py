# Este método hace una traduccion de los keycodes de caracteres

# Principalmente esto keycodes se encuentran en diccionarios y se hace uso del método maketrans para crear estos diccionarios

# Una de sus funciones principales es reemplazar caracteres de un string o eliminar caracteres

nombre = "corazon"
conversion = nombre.maketrans("cz", "md", "n")
print(conversion) # {99: 109, 122: 100, 110: None}

# Este es el diccionario que contiene los keycodes y es el que el método translate traduce por medio de un string

nombre_cambiado = nombre.translate(conversion) # conversion es el diccionario
print(nombre_cambiado, "\n") # morado

palabra = "zarcillo"

nombre_cambiado = palabra.translate(conversion)
print(nombre_cambiado) #darmillo

# Este sería el uso mas común del método translate