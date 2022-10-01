from os import system, name


def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "ce" or name == "nt" or name == "dos":
        system("cls")


def entero(num):
    """Convierte un numero binario a entero
    
    num string cualquier numero
    returns un numero binario
    """

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
    """Convierte un numero entero a binario

    num int cualquier entero
    returns un numero entero
    """
    
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

    while True:
        while True:
            try:
                print("""Conversiones:
                
    1) Conversion binario-entero
    2) Conversion entero-binario
            """)

                opcion = int(input("Digite un modo de conversion: "))

                if opcion != 1 and opcion != 2:
                    limpiar_pantalla()
                    print("Elija la opcion 1 o 2\n")
                else:
                    break

            except ValueError:
                limpiar_pantalla()
                print("Elija la opcion 1 o 2\n")

        if opcion == 1:
            while True:
                num = input("\nDigite un número binario: ")

                if num.count("0") + num.count("1") < len(num):
                    limpiar_pantalla()
                    print("Solo digite numeros 1 y 0")
                else:
                    break

            num_entero = entero(num)
            print(f"El número binario {num} a número entero es {num_entero}\n")
            
        elif opcion == 2:
            while True:
                try:
                    num = int(input("\nDigite un número entero: "))
                    break
                except ValueError:
                    limpiar_pantalla()
                    print("Valor no válido...")

            num_binario = binario(num)
            print(f"El número {num} a binario es: {num_binario}\n")


        # Hacer otra conversion

        while True:
            continuar = int(input("¿Quieres hacer otra conversion? 1(si) 2(no): "))

            if continuar == 2:
                print()
                break
            elif continuar != 1:
                limpiar_pantalla()
                print("Valor no válido...\n")
            else:
                limpiar_pantalla()
                break
        if continuar == 2:
            break
        

if __name__ == "__main__":
    run()