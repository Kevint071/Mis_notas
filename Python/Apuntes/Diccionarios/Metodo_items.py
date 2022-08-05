diccionarios = {
    "Edad": 15,
    "Genero": "M"
}

print(diccionarios.items()) # dict_items([('Edad', 15), ('Genero', 'M')])

for llave, valor in diccionarios.items():
    print(f"Su {llave} es: {valor}")

    # Su Edad es: 15
    # Su Genero es: M