# La palabra clave "pass", funciona como relleno cuando se quiere hacer algo en una parte del codigo pero en un futuro

if 1 != 2:
    pass
else:
    print(1 == 2)

# Con el ejemplo de arriba aqui se usa para después colocar algo donde dejaste a esa palabra:

if 1 != 2:
    print("El número 1 es diferente al numero 2") # Aqui iba pass
else:
    print(1 == 2)
