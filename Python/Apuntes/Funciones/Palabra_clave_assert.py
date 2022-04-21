# La palabra clave assert son afirmaciones que se usan para defendernos de las entradas que pueda hacer una persona con un input

def primer_letra(lista_de_palabras):
    primeras_letras = []

    print(lista_de_palabras)

    for i in lista_de_palabras:
        assert type(i) == str, f"{i} no es un string"
        assert len(i) > 0, "El string no puede estar vacio"

        primeras_letras.append(i[0])
    
    return primeras_letras

cantidad_palabras = int(input("Digite la cantidad de palabras que quiere escribir: "))
lista_de_palabras = []

for i in range(1, cantidad_palabras+1):
    palabra = input(f"Digite la palabra {i}: ")
    lista_de_palabras.append(palabra)

print(primer_letra(lista_de_palabras))


