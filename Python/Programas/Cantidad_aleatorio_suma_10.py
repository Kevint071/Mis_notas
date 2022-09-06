import random

lista = []

for i in range(249):
    num = random.randint(0, 9)
    lista.append(str(num))

acum = 0

suma_10 = []
posiciones = []

for i in range(0, len(lista)):

    if i == len(lista)-1:
        break

    if int(lista[i]) + int(lista[i+1]) == 10:
        posiciones.append([i+1, i+2])
        acum += 1
        suma_10.append([int(lista[i]), int(lista[i+1])])
        
print(f"\n{''.join(lista)}\n")
print(f"La cantidad de sumas que hay son: {acum}\n")
print(f"Lista de las sumas: {suma_10}\n")

ver_pos = int(input("¿Desea ver las posiciones? 1(si) 2(no): "))

if ver_pos == 1:
    print(f"\nLista de posiciones: {posiciones}")
