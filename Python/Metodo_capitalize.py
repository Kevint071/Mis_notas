# Convierte la primera letra de la cadena de caracteres en mayúscula

lugar = "colombia"

lugar = lugar.capitalize()
print(lugar) # Colombia

# Si hay un caracter al inicio del string que no sea letra el metodo no hace ninguna modificacion al string

nombre = " kevin".capitalize()
print(nombre) #  kevin

# No convierte a mayúscula la primera letra de otra palabra en la misma cadena de caracteres

mensaje = "hola kevin"

mensaje = mensaje.capitalize()
print(mensaje) # Hola kevin
