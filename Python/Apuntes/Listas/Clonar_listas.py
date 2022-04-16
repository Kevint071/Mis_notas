# Es importante clonar listas en vez de mutarlas o copiarlas

# Ejemplo de que pasa si se copia

a = ["a", "b", "c"]
b = a

print(a is b) # True 

# Las 2 listas tienen el mismo id por lo que al editar una lista, se edita la otra

a.append("d") 

print(a) # ["a", "b", "c", "d"]
print(b) # ["a", "b", "c", "d"]

# Para evitar esto hay 2 formas:

# 1. Copiarla como slice

c = a[::]

print(a is c) # False

a.pop()

print(a) # ["a", "b", "c"]
print(c) # ["a", "b", "c", "d"]

# 2. Copiarla como tipo de dato list()

d = list(a)

print(a is d) # False

a.append("d") 

print(a) # ["a", "b", "c", "d"]
print(d) # ["a", "b", "c"]




