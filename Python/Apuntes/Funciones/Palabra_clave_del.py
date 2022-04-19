# del se usa para borrar un valor de una variable, por medio del índice o borrar variables enteras

lista = [1, 2, 3, 4, 5, 6, 7]
del lista[2] # Borra el indice 2 de la lista

print(lista) # [1, 2, 4, 5, 6, 7]

del lista # Borra la variable

print(lista) # lista is not defined

# Borra cualquier tipo de dato

num = 43

del num
print(num) # num is not defined

dic = {
    "nombre":"Kevin",
    "edad": 99
}

del dic["edad"]

print(dic) # {'nombre': 'Kevin'}

del dic

print(dic) # dic is not defined



