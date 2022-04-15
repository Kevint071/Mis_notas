# choice(), del módulo random, elige un valor al azar de un tipo de dato string o lista

import random

lista = [1, 2, 3, 4, 5]

valor_lista = random.choice(lista)
print(valor_lista)

nombre = "Kevin"
letra = random.choice(nombre)
print(letra)

# Pasar a archivo random.random()

print(round(random.random() * 100, 2))