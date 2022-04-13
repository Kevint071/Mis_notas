from random import randint
lista_usuario = []
si_no = 1

while si_no == 1:

    win = None
    lista_usuario.clear()    
    numero = randint(1, 30)
    i = 0

    while i < 7:
        i += 1
        while True:
            try:
                num_usuario = int(input("Intenta adivinar el número que pienso entre 1 y 30: "))
                lista_usuario.append(num_usuario)

                numero_menos_1 = numero - 1 in lista_usuario
                numero_mas_1 = numero + 1 in lista_usuario

                if numero_menos_1 == True and numero_mas_1 == True:
                    print(f"Como ya has elegido el número {numero-1} y el {numero+1} ovbiamente el número que pienso es el {numero} así que has ganado\n")
                    win = 0
                    break
                
                if lista_usuario.count(num_usuario) == 2:
                    print("Este número ya lo había dicho, piense otro\n")
                    lista_usuario.remove(num_usuario)
                elif num_usuario > 30 or num_usuario < 1:
                    print("El número que debes adivinar está entre 1 y 30\n")
                else:
                    break 
            except:
                print("Número no válido")

        if numero_menos_1 == True and numero_mas_1 == True:
            break
        elif numero - 1 == 0  and numero_mas_1 == True:
            print(f"Como ya has elegido el número {numero+1} ovbiamente el número que pienso es el {numero} así que has ganado\n")
            win = 0
            break

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