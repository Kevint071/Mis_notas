palabra = input("Digite una palabra: ")
palabra = palabra.lower()

silabas = []
codigo_palabra = []

consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

lista_palabra = list(palabra)

print(lista_palabra)

cantidad_vocales = 0
cantidad_consonantes = 0

for i in palabra:
    if i in vocales:
        cantidad_vocales += 1
        codigo_palabra.append("1")
        
    elif i in consonantes:
        cantidad_consonantes += 1
        codigo_palabra.append("0")

print(f"\nHay {cantidad_vocales} vocales")
print(f"hay {cantidad_consonantes} consonantes")

palabra_code = "".join(codigo_palabra)
print(palabra_code)

# Sin temrinar