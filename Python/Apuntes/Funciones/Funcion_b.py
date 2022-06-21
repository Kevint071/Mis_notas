# La funcion \b sirve para hacer un backspace en la linea en la que se ejecute

print("Hola\b" + "a a todos") # Se elimina la "a" de la cadena "Hola"

# Para que la funcion pueda notarse luego en esa misma linea debe mostrarse otro dato

lista = [1, 2, 3]

print(f"Esta es la lista: " +  "\b" * 10 + f"{lista}") # Esta es [1, 2, 3]

# Por ejemplo se puede mostrar una lista, y en este caos se eliminan 10 espacios

# Otra manera de usar \b es la siguiente

print("Hola 323", end = "")  # Se termina el print, continuando en la misma linea
print("\b" * 3 + "a todos") # Se eliminan 3 caracteres y se agrega la cadena de caracteres que sigue

# Resultado: Hola a todos