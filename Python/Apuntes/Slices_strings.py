# Para acceder a un caracter especifico de un string se hace lo siguente:

nombre = "Cristian"
print(nombre[0]) # C
print(nombre[1]) # r

# Los números son las posiciones de los strings que van desde 1 hasta la cantidad de caracteres que haya en el string

print(nombre[7]) # n

# Además de las posiciones positivas tambien hay posiciones negativas

print(nombre[-1]) # n
print(nombre[-2]) # a
print(nombre[-4]) # t

# Estas posiciones van desde la posicion -1 hasta la cantidad de caracteres que haya en el string y si se quieren obtener mas de un solo caracter se usan los 2 puntos ":"

# El primer parametro antes de los ":" es la posicion desde la que se quiere comenzar y el parametro que va despues de los ":" es la posicion hasta la que se quiere llegar

print(nombre[0:2]) # Cr
print(nombre[3:7]) # stia

# Además tambien se pueden usar numeros negativos

print(nombre[-5: 6]) # sti
print(nombre[-8:4]) # Cris

# Lo que no se puede hacer es colocar una posicion inicial que esté despues de la posicion final ya que en esos casos no agarraría ningun valor, como por ejemplo:

print(nombre[-3:2]) # 
print(nombre[-6:1]) # 

# Hay un tercer parámetro el cual sirve para indicar la cantidad de pasos que se haran para llegar al número final, además de agregar el sentido en el cual irá

print(nombre[1:6:2]) # rsi
print(nombre[1:6:1]) # risti

# Para devolver valores en reversa se coloca el ultimo valor negativo

print(nombre[7:-6:-2]) # nist
print(nombre[6:-4:-1]) # ai

# Para decidir la cantidad de pasos que se van a recorrer se coloca el tercer parámetro diferente a 1

print(nombre[0:6:2]) # Cit
print(nombre[1:5:2]) # rs

# Para obtener todos los caracteres en reversa se hace lo siguiente:

print(nombre[::-1]) # naitsirC

# Para obtener todos los caracteres en sentido normal se hace lo siguiente

print(nombre[::1]) # Cristian

# El valor por defecto del parametro 3 es positivo con paso 1

print(nombre[::]) # Cristian

# Para guardar slices se hace lo siguiente

variable = nombre[0:3]
variable = nombre[::-1]
