# Para reemplazar valores en un string se usa el método replace()

print("Usando el metodo replace():")

nombre = "keiner"

nombre = nombre.replace("e", "u")
print(nombre) # kuinur

nombre = nombre.replace("u", "")
print(nombre) # kinr

# Para quitar espacios adicionales en un string se usa el método strip()

print("\nUsando el metodo strip():")

nombre = " keiner "

nombre = nombre.strip()
print(nombre) # keiner

# Tambien se puede decidir desde que lado se quitaran los espacios

nombre = " keiner "

# rstrip quita los espacios innecesarios de la derecha y lstrip los espacios innecesarios de la izquierda

nombre = nombre.rstrip()
print(nombre) #  keiner

nombre = nombre.lstrip()
print(nombre) # keiner

# Además de quitar espacios, el metodo strip tambien puede quitar caracteres

nombre = "alicia"

nombre = nombre.strip("a")
print(nombre) # lici

# O tambien se puede decidir desde que lado quitar los caracteres

nombre = "alicia"

nombre = nombre.rstrip("a")
print(nombre) # alici

# Para contar cuantos caracteres hay en una cadena de caracteres se usa el método len()

print("\nUsando el metodo len():")

nombre = "juan"

cantidad_letras = len(nombre)
print(cantidad_letras) # 4
