# remove() se utiliza cuando se quiere remover un valor de una lista pero por su valor, no por el índice

lista = [2, 3, 4, 1, 5, 6, 3, 4]

lista.remove(3)
print(lista) # [2, 4, 5, 1, 5, 6, 3, 4]

# Para eliminar todos los valores, se usará un ciclo for y la función de lista count() "mirar en el archivo metodo_count.py"

lista = [2, 3, 4, 1, 5, 6, 3, 4]

for i in range(lista.count(4)):
    lista.remove(4)

print(lista) # [2, 3, 1, 5, 6, 3]

# Otra manera de hacerlo es lo siguiente:

lista = [2, 3, 4, 1, 5, 6, 3, 4]

for i in range(len(lista)-1, -1, -1):
    if lista[i] == 4:
        lista.remove(4)

print(lista) # [2, 3, 1, 5, 6, 3]

# Lo que se hace en este ejemplo es crear un rango que tenga de valor inicial: la cantidad de valores en la lista. De rango final: el último valor de la lista, y que vaya en sentido negativo. Ya con eso, la variable iteradora "i" en lista[i], irá desde el último valor de la lista hasta el valor inicial recorriendo la lista inversamente. Como el rango no agarra el último valor de range (-1), quedaría como si el valor final fuera el valor inicial, osea indice 0.