# Las list comprenhensions sirven para editar valores de una lista o para filtrar valores

# 1. Multiplicar todos los numeros de una lista por 2

lista = list(range(1, 6))
print("Numeros de una lista: ", lista) # [1, 2, 3, 4, 5]

lista_num_doble = [i * 2 for i in lista]
print("Los mismos números pero dobles: ", lista_num_doble) # [2, 4, 6, 8, 10]

# 2. Extraer los numeros pares de una lista

lista = list(range(1, 11))
print("\nNumeros de una lista", lista) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_par = [i for i in lista if i % 2 == 0]
print("Los mismos números pero filtrados: ", lista_par) # [2, 4, 6, 8, 10]