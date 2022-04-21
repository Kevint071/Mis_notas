# Esta excepción se usa cuando se intenta dividir un número entre 0

lista = [1, 4, 3, 0]
lista_division = []

try:
    for i in lista:
        lista_division.append(4/i) # 4/número de la lista
except ZeroDivisionError:
    print("Error, hay 0 dividiendo en la lista")