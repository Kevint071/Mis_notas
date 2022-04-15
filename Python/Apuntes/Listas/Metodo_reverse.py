# reverse sirve para devolver una lista sino que en reversa

lista = [1, 2, 3, 4, 5, 6]
lista.reverse()

print(lista) # [6, 5, 4, 3, 2, 1]

lista = ["H", "o", "l", "a"]
lista.reverse()

print(lista)

# También hay otra manera de hacerlo con un ciclo for:

lista = [1, 2, 3, 4, 5, 6]
lista_reversa = []

for i in range(len(lista)-1, -1, -1):
    lista_reversa.append(lista[i])
print(lista_reversa)

# A diferencia del metodo reverse(), en este modo de hacerse hay que crear otra lista por lo que lo mas óptimo aveces es trabajar con el método reverse()