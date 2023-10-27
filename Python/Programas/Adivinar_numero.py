from random import randint
from os import system, name


def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "nt" or name == "dos" or name == "ce":
        system("cls")


def adivinar_numero(lista_usuario):
    # Se digita el numero y en caso de errores se mandan mensajes a la consola
    while True:
        try:
            num_usuario = int(input("Intenta adivinar el número que pienso entre 1 y 30: "))
            lista_usuario.append(num_usuario)
            
            if lista_usuario.count(num_usuario) == 2:
                print("Este número ya lo había dicho, piense otro\n")
                lista_usuario.remove(num_usuario)
            elif num_usuario > 30 or num_usuario < 1:
                print("El número que debes adivinar está entre 1 y 30\n")
            else:
                break 
        except:
            print("Número no válido")
    return num_usuario


def comparar_numero(num_usuario, numero):
    win = False
    if num_usuario > numero:
        print("El número en que pienso es mas bajo...\n")
    elif num_usuario < numero:
        print("El número en que pienso es mas alto...\n")
    else:
        print("Has acertado!\n")
        win = True
    return win


def volver_a_jugar():
    while True:
        try:
            desicion = int(input("¿Desea jugar otra vez? 1(si) 2(no): "))

            if desicion == 1 or desicion == 2:
                print()
                break
            else:
                print("El número no es válido\n")
        except:
            print("Esto no es un número\n")
    return desicion


def inicio_juego(lista_usuario, numero, i):
    while i < 6:
        i += 1
        num_usuario = adivinar_numero(lista_usuario)

        # Se dice si el número digitado por el usuario es mayor o menor o igual

        win = comparar_numero(num_usuario, numero)
        if win == True:
            return win
    return win

def run():
    lista_usuario = []
    desicion = 1

    while desicion == 1:
        limpiar_pantalla()
        win = None
        lista_usuario.clear()    
        numero = randint(1, 30)
        i = 0

        # Se crea el ciclo while con 6 intentos, representados por la variable i

        win = inicio_juego(lista_usuario, numero, i)

        if win == False:
            print(f"Perdistes... El número en que pensaba era el {numero}\n")
        
        # En caso de querer volver a jugar

        desicion = volver_a_jugar()


if __name__ == "__main__":
    run()