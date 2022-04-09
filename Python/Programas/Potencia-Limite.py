def potencias_de_2(LIMITE):
    contador = 0

    while 2 ** contador <= LIMITE:
        contador += 1
    return contador


def run():
    limite = int(input("Digite un numero menor o igual a una potencia de 2: "))

    exponente_limite = potencias_de_2(limite)

    print(f"\nEl exponente que no sobrepasa el limite digitado es el número {exponente_limite-1}:\n")

    for i in range(0, exponente_limite):
        print(f"La potencia de 2 a la {i} es {2 ** i}")


if __name__ == "__main__":
    run()