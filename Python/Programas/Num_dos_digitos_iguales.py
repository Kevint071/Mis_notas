def run():

    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    acum = 0

    for i in range(1, 2001):
        for j in lista:
            if str(i).count(str(j)) == 2:
                acum += 1
                print(i)
                break
    
    print(f"Hay {acum} numeros con dos cifras iguales")

if __name__ == "__main__":
    run()