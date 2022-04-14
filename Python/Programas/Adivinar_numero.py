from random import randint


def run():
    lista_usuario = []
    si_no = 1

    while si_no == 1:

        win = None
        lista_usuario.clear()    
        numero = randint(1, 30)
        i = 0

        # Se crea el ciclo while con 6 intentos, representados por la variable i

        while i < 6:
            i += 1

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

            # Se dice si el número digitado por el usuario es mayor o menor o igual

            if num_usuario > numero:
                print("El número en que pienso es mas bajo...\n")
            elif num_usuario < numero:
                print("El número en que pienso es mas alto...\n")
            else:
                win = "Has acertado!\n"
                print(win)
                break

        if win == None:
            print(f"Perdistes... El número en que pensaba era el {numero}\n")
        
        # En caso de querer volver a jugar
            
        while True:
            try:
                si_no = int(input("¿Desea jugar otra vez? 1(si) 2(no): "))
                
                if si_no == 1 or si_no == 2:
                    print()
                    break
                else:
                    print("El número no es válido\n")
            except:
                print("Por Dios esto no es un número\n")


if __name__ == "__main__":
    run()