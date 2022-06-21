# Para desempaquetar una lista se usa el símbolo *

lista = [1, 2, 4, "Hola"]

print(*lista) # 1 2 4 Hola
print(lista)

# Ejemplo de uso

lista= ["este", "este también"]
tupla= ("este", " y este")

print("Hola el uso de desempaquetar un conjunto de datos es %s y %s, además de %s%s"%(*lista,  *tupla))

# Se puede observar que funciona tanto para listas como para tuplas

# Ejemplo de uso con funcion

def sumar_numeros(*numeros):

    # Se suman los números contenidos en una tupla por medio de un ciclo for

    acum = 0
    for i in numeros:
        acum += i
    
    return acum

suma_numeros = sumar_numeros(2, 4, 5, 6, 3)

print(suma_numeros) # 20
