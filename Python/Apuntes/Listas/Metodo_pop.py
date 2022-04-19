# Este metodo se aplica con listas y sirve para eliminar por el índice, un valor.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 4, 3]

# Cuando pop no tiene un parámetro, por defecto elimina el último valor de la lista:

lista.pop() # Se elimina el último valor de la lista (3)

print(lista) # [1, 2, 3, 4, 5, 6, 7, 8, 4]

# Para eliminar un valor específico por el índice se le añade un parámetro a pop():

lista.pop(2) # Se elimina el valor con íncide 2 (3)

print(lista) # [1, 2, 4, 5, 6, 7, 8, 4]

lista.pop(1)

# Uno puede ver el valor que elimina pop()

print(lista.pop()) # 4
print(lista) # [1, 4, 5, 6, 7, 8]

print(lista.pop(2)) # 5
print(lista) # [1, 4, 6, 7, 8]