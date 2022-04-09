# Se utiliza not para usar el booleano contrario que esté en ese momento

es_dia = True
es_noche = False

# Se usa \n para hacer un salto de linea

print("Mostrar los valores booleanos sin 'not':\n")

print(es_dia)
print(es_noche)

print("\nMostrar los valores booleanos con 'not':\n")

print(not es_dia)
print(not es_noche)

# Se utiliza not para saber si un valor está en una lista

lista = [1, 2, 6, 9, 3]

print(f"\n{lista}")

if 4 not in lista:
    print("\nEl número 4 no está en la lista")
else:
    print("\nEl número 4 está en la lista")

# Tambien se puede negar un valor booleano sin tener que hacerlo por medio de una variable

if 1 != 2:
    print()
    print(not True)

