diccionarios = {
    "Edad": 15,
    "Género": "M"
}


# Para obtener las keys de un diccionario se usa la funcion keys:

print(diccionarios.keys()) # dict_keys(['Edad', 'Género'])

# Si quereos mostrar las llaves de una forma mas ordenada hacemos lo siguiente:

for i in diccionarios.keys():
    print(f"Key: {i}")


# Resultado

#    Key: Edad
#    Key: Género
