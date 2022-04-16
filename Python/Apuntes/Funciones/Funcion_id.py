# EL id es una direccion que se le da a una variable

saludo = "Hola"
print(id(saludo))

saludo_2 = "Que tal"
print(id(saludo_2))

# Los id son diferentes en cada variable, y en algunos casos pueden ser muy parecidos

# La manera de tener 2 variables con el mismo id es la siguiente:

nombre = "Kevin"
nombre_inicial = nombre

print(id(nombre))
print(id(nombre_inicial))
