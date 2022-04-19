# El método get devuelve el valor de una clave que manualmente se le asigna si no está una llave en el diccionario, y si está la llave, se muestra el valor de esta.

genero = {
    "Juana": "Femenino",
    "Juan": "Masculino",
    "Manuel": "Masculino",
    "Lucía": "Femenino"
}

respuesta = genero.get("Jaime", "No se encuentra el nombre")
print(respuesta) # No se encuentra el nombre

respuesta = genero.get("Lucía", "No se encuentra el nombre")
print(respuesta) # F

input("\nPresione enter para continuar... ")

# El primer parámetro es el valor de la llave y el segundo es la respuesta que se da si no se encuentra la llave en el diccionario

# Digitando un nombre para obtener una respuesta de get

nombre = input("Digite el nombre: ")

respuesta = genero.get(nombre, f"No se encuentra el nombre {nombre}")
print(respuesta)