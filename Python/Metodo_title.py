# El metodo title convierte la primera letra de cada palabra en mayúscula

nombre = "kevin"

nombre = nombre.title()
print(nombre) # kevin

mensaje = "hola mundo"

mensaje = mensaje.title()
print(mensaje) # Hola Mundo

# Este método no toma en cuenta los espacios como si lo hace el metodo capitalize

nombre = " kevin"

nombre = nombre.title()
print(nombre) #  Kevin