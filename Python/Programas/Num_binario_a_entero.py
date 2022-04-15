def entero(num):
    # Se guardan la cantidad de valores del numero binario para luego usarlos como exponentes

    cantidad_numeros = range(len(num))

    exponentes = list(cantidad_numeros)
    exponentes.reverse()

    # Sumando las potencias de 2 si el valor de el numero binario contiene 1, si contiene 0 no se suman.

    acumulado = 0

    for i in cantidad_numeros:
        if num[i] == "1":
            acumulado += 2 ** exponentes[i]
    
    return acumulado

def binario(num):
    # Hallar limite de exponente con base 2. La potencia no puede superar al número entero
    
    exponente = 0

    while 2 ** exponente <= num:
        exponente += 1
    
    # Acumular la potencia que es menor a el número entero y luego esa potencia sumarla con la que sigue, si el resultado es mayor no se guarda y la potencia sigue quedando igual.

    acumulado = 0
    numero_binario = []

    for i in range(exponente-1, -1, -1):
        acumulado_actual = 2 ** i + acumulado
        if acumulado_actual <= num:
            acumulado += 2 **i
            num_binario = 1
        else:
            num_binario = 0
        numero_binario.append(str(num_binario))
    
    numero_binario = "".join(numero_binario)

    return numero_binario

def run():

    print("""Conversiones:
    
    1) Conversion binario-entero
    2) Conversion entero-binario
    """)

    opcion = int(input("Digite un modo de conversion: "))

    if opcion == 1:
        while True:
            num = input("Digite un número binario: ")

            if num.count("0") + num.count("1") < len(num):
                print("Solo digite numeros 1 y 0\n")
            else:
                break

        num_entero = entero(num)
        print(f"El número binario {num} a número entero es {num_entero}")
        
    elif opcion == 2:
        num = int(input("Digite un número entero: "))
        num_binario = binario(num)
        print(f"El número {num} a binario es: {num_binario}")

if __name__ == "__main__":
    run()