# Este método sirve para reemplazar caracteres de un string, con otro string y almacena estas conversiones como tipo diccionario

# En este código, las vocales con tildes o caracteres especiales serán reemplazadas con los otros caracteres

vocal = "aaeeiioouuaeeiioouu"
vocal_tilde = "áäéëíïóöúüÁÉËÍÏÓÖÚÜ"
quitar_tilde = str.maketrans(vocal_tilde, vocal)

print(quitar_tilde)

# En este código se pasa de el contenido de la variable "mayusculas" a "minusculas"

mayusculas, minusculas = "AEIOU", "aeiou"
metodo_lower = str.maketrans(mayusculas, minusculas)

print(metodo_lower) # {65: 97, 69: 101, 73: 105, 79: 111, 85: 117} Este es el resultado en forma de diccionario

# Es importante saber que deben haber la misma cantidad de letras en los 2 parámetros de maketrans para que la conversion se pueda realizar

# En este codigo se van a reemplazar la letra a por la letra e

oracion = "Mi mama me mima"
conversion_vocal = oracion.maketrans("ma", "se") # Se cambia la letra "m" por la "s" y la letra "a" por la "e"

print(conversion_vocal) # {109: 115, 97: 101}

# Con lo siguiente se analiza que los diccionarios contienen las keycodes de las teclas que nosotros asignamos en los parámetros de maketrans

# Por lo tanto si creamos un diccionario con keycodes de letras que queremos cambiar, igualmente funcionaria

saludo = "Hola me llamo kevin"
vocales_a_o = {97: 101, 105: 111} # Conversion keycode 95 (letra a) a keycode  101 (letra e) y de el keycode 105 (letra i) a keycode 111 (letra o)

print(vocales_a_o) # {97:101, 105:111}

# Se observa que arroja una respuesta similar que con el método maketrans

# Además, el método maketrans posee un tercer parámetro el cual sirve para eliminar carácteres de el texto

saludo = "Hola mundo"
convertir = saludo.maketrans("oa", "eo", "dm")
print(convertir) # {111: 101, 97: 111, 100: None, 109: None}

convertir = saludo.maketrans("oa", "eo", "uo")
print(convertir) # {111: None, 97: 111, 117: None}

convertir = saludo.maketrans("au", "oa", "uos")
print(convertir) # {97: 111, 117: None, 111: None, 115: None}

# Lo primero que se hace en este proceso es colocar en primer lugar los keycodes del parámetro 1

# Mientras se colocan, se revisa que no los caracteres del parámetro 1 no estén en el parámetro 3

# Si los caracteres del parámetro 1 están en el parámetro 3, no habrá conversión con el parámetro 2 y habrá conversion con (parametro 1) y (None)

# Luego de esto se colocan en el diccionario los caracteres del parámetro 3 que no estén en el parámetro 1 ya que si alguno está en el parametro 1, entonces este pasará a la posicion del parámetro 1 en el diccionario (osea en la posicion donde debia ir el parámetro 1)

# Luego, se colocan los caracteres del tercer parámetro pasando del caracter del tercer parámetro a None (ningun valor), por lo tanto se elimina el caracter.

# Para reemplazar estos caracteres se usa el método translate