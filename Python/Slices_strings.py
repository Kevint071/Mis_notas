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

# Solo me muestra la posicion 0 y 1 ya que el parámetro final agarra una posicion anterior a la que le pusimos, en este caso cogió desde la posicion 0 a la posición 1

print(nombre[3:7]) # stia

# Además tambien se pueden usar numeros negativos

print(nombre[-5: 6]) # sti
print(nombre[-8:4]) # Cris

# Lo que no se puede hacer es colocar una posicion inicial que este despues de la posicion final ya que en esos casos no agarraría ningun valor, como por ejemplo:

print(nombre[-3:2]) # None
print(nombre[-6:1]) # None

# Además de esto, hay un tercer parámetro el cual sirve para indicar la cantidad de pasos que se haran para llegar al número final, además de agregar el sentido en el cual irá

print(nombre[7:-6:-1]) # naist
print(nombre[6:-4:-1]) # ai

# Como se puede ver devuelve valores en reversa ya que se va desde una posicion mayor hasta una posicion menor con sentido negativo debido al ultimo parámetro negativo

print(nombre[0:6:2]) # Cit
print(nombre[1:5:2]) # rs

# Aqui se observa que va de 2 en 2 pasos, por lo tanto acepta un caracter y rechaza otro y asi sucesivamente hasta llegar al parámetro final. Como se observa va en sentido positivo

# Para obtener todos los caracteres en reversa se hace lo siguiente:

print(nombre[::-1]) # naitsirC   # Sentido en negativo
print(nombre[::1]) # Cristian    # Sentido positivo

# Se observa que los valores por defecto de el parametro 1 y 2 varian de acuerdo al parámetro 3 y el valor por defecto del parametro 3 es positivo con paso 1

print(nombre[::]) # Cristian


