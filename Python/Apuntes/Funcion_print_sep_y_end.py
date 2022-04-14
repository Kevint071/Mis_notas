# La funcion print muestra un valor y tiene 2 argumentos los cuales son end y sep

print("Hola")

# El argumento end sirve para modificar el ultimo valor de print() que por defecto es \n, es decir el valor de end por defecto es \n

print("Hola mundo", end=" ")
print("Lindo") # Hola mundo Lindo

print("Hola mundo", end="")
print("s") # Hola mundos

# El argumento sep sirve para unir a dos o mas cadenas de caracteres. El valor de sep por defecto es un espacio

print("Hola", "mundo") # Hola mundo
print("Hola", "mundo", sep= " ") # Hola mundo
print("Hola", "todos", sep= " a ") # Hola a todos

# Tambien se pueden usar los 2 argumentos juntos

print("Hola, la fecha de hoy es: " + "8", "04", "2022.", sep="-", end=" ")
print("Buen dia")

# Como se observa, sep solo funciona cuando los strings están separador por coma y no por el signo "+", ya que este signo une a los strings al momento de ejecutarse.

