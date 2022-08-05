diccionarios = {
    "Edad": 15,
    "Género": "M"
}


# Para obtener las keys de un diccionario se usa la funcion keys:

print(diccionarios.values()) # dict_values([15, 'M'])

# Si quereos mostrar las llaves de una forma mas ordenada hacemos lo siguiente:

for i in diccionarios.values():
    print(f"Valor: {i}")

    # Valor: 15
    # Valor: M
    