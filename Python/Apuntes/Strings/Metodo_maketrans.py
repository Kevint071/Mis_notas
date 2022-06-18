# Este método sirve para reemplazar caracteres de un string, con otro string y almacena estas conversiones como tipo diccionario

# En este código, las vocales con tildes o caracteres especiales serán reemplazadas con los otros caracteres

vocal = "aaeeiioouuAEEIIOOUU"
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

# Para reemplazar estos caracteres se usa el método translate