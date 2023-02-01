lista_num = [1, 2, 3, 4, 5, 6, 7, 8]
lista_resultado = [[]]

for num in lista_num:

    lista_nueva = [i + [num] for i in lista_resultado]    
    lista_resultado += lista_nueva

print(lista_resultado)
