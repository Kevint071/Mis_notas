# El operador is sirve para comparar 2 objetos por su id

Hola = "Hola"
Hola_2 = "Hola"

print(id(Hola))
print(id(Hola_2))

print(Hola is Hola_2) # True

a = [1, 2, 3]
b = [1, 2, 3]

print()

print(a is b) # False

a = (1, 2, 3)
b = (1, 2, 3)

print(a is b) # True

# Con valores inmutables e iguales is arroja el resultado True pero si son valores mutables e iguales, is arroja el valor False

# is arroja False cuando los id de las 2 variables son diferentes entre si
# is arroja True cuando los id de las 2 variables son iguales entre si, pero esot significa que las 2 variables apuntan a un solo objeto