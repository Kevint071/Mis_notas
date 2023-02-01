import time

tiempo_desde_1970 = time.time()

# Este método del módulo time, es muy útil para medir el tiempo de proceso de un programa:

# Aquí se muestra este ejemplo

inicio = time.time()

print("Hola")
print("Estas son dos impresiones")

fin = time.time()

# Se resta el tiempo tomado en el inicio y el tiempo tomado al final para ver la duracion de la impreison de dos lineas de codigo

print(f"El tiempo de ejecucion fue de {fin - inicio} segundos")