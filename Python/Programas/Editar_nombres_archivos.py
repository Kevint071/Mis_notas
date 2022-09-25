import os


def pedir_informacion(accion, opcion_3):

    # Esta funcion solo aplica cuando se agrega o borra caracteres
    # No se aplica (usa) cuando se reemplazan caracteres

    insertar = int(input(f"""\n¿Donde quieres {accion} los caracteres?:
    
                1. Inicio
                2. Final
                3. {opcion_3}
                
                : """))
    
    if insertar == 3 and opcion_3 == "Posicion específica":
        posicion = int(input("""\nDigite el numero de la posicion que quiere insertar: 
        
            Ejemplo: 

            Nombre archivo: Hola.py
            Caracter 'a'
            Posicion: 2

            Resultado: Hoala.py

            : """))
        
        # Si la persona quiere agregar caracteres se returna con la variable insertar y posicion
    
        return (insertar, posicion)
    return (insertar, None)


def agregar_caracteres(directorio, i, caracteres, insertar, posicion):

    """Función que agrega caracteres a los nombres de archivos
    parametros directorio tipo directorio, string i, string caracteres, int insertar, int posicion
    returns None"""

    nombre = []

    for letra in i:
        nombre.append(letra)
    
    
    if insertar == 1:
        nombre.insert(0, caracteres)
        nombre = "".join(nombre)
    elif insertar == 2:
        nombre.append(caracteres)
        nombre = "".join(nombre)
    elif insertar == 3:
        nombre.insert(posicion, caracteres)
        nombre = "".join(nombre)

    os.rename(f"{directorio}/{i}", nombre)


def borrar_caracteres(directorio, i, caracteres, insertar):
    
    if insertar == 1:
        os.rename(f"{directorio}/{i}", i.lstrip(caracteres))
    elif insertar == 2:
        os.rename(f"{directorio}/{i}", i.rstrip(caracteres))
    elif insertar == 3:
        if len(caracteres) > 1:
            for j in caracteres:
                os.rename(f"{directorio}/{i}", i.replace(j, ""))
                i = i.replace(j, "")


def reemplazar_caracteres(directorio, i, caracteres, reemplazo):

    # Ciclo que recorre los caracteres y sus reemplazos y los aplica en los nombres de archivos

    for caracter, su_reemplazo in zip(caracteres, reemplazo):
        os.rename(f"{directorio}/{i}", i.replace(caracter, su_reemplazo))
        i = i.replace(caracter, su_reemplazo)
    

def interior_dir(directorio, opcion, caracteres, reemplazo, insertar, posicion):

    """Función que recorre todas las carpetas y subcarpetas
       Parámetro 'directorio' es cualquier directorio Ej: /home/user/Documentos
       returns None"""

    print(f"\nDirectorio: {directorio}\n")

    directorio_interior = os.listdir(directorio)

    # Excluyendo la carpeta de gestion de versiones (git)

    if directorio_interior.count(".git"):
        directorio_interior.remove(".git")
    
    # Verificando si es archivo o carpeta
    # Si es carpeta entra en esa carpeta y busca archivos (accion con recursividad)

    for i in directorio_interior:

        if os.path.isdir(f"{directorio}/{i}") == True:
            interior_dir(f"{directorio}/{i}")
        else:
            if opcion == 1:
                agregar_caracteres(directorio, i, caracteres, insertar, posicion)
            elif opcion == 2:
                borrar_caracteres(directorio, i, caracteres, insertar)
            elif opcion == 3:
                reemplazar_caracteres(directorio, i, caracteres, reemplazo)


def run():

    # Obtener el directorio que digita el usuario

    directorio = input('Digite el directorio al que desea cambiarle los nombres de los archivos: ')
    directorio_principal = os.chdir(directorio)
    directorio_principal = os.getcwd()
    print(directorio_principal)

    # Ciclo para repetir la edicion de nombres

    while True:

        # Elegir que tipo de edicion de nombre de archivos quiere el usuario

        opcion = int(input("""\nElija lo que desea editar de los nombres de archivos...
        
        1. Agregar caracteres 
        2. Borrar caracteres 
        3. Reemplazar caracteres

        : """))

        if opcion == 1:
            accion = "agregar"
        elif opcion == 2:
            accion = "borrar"
        elif opcion == 3:
            accion = "reemplazar"

        caracteres = input(f"\nDigita el caracter que quieres {accion}: ")

        # Pidiendo informacion detallada sobre como se hará de la edicion de nombre

        if opcion == 1 or opcion == 2:
            if opcion == 1:
                insertar, posicion = pedir_informacion(accion, "Posicion específica")
            else:
                insertar, posicion = pedir_informacion(accion, "En todo el nombre")

            interior_dir(directorio_principal, opcion, caracteres, None, insertar, posicion)
            print("Operacion completada...\n")
        elif opcion == 3:
            reemplazo = input("Digite un caracter para reemplazar el caracter anterior: ")
            interior_dir(directorio_principal, opcion, caracteres, reemplazo, None, None)

        desicion = int(input(f"¿Desea volver a editar el archivo? 1(si) 2(no): "))

        if desicion == 2:
            break

if __name__ == "__main__":
    run()

