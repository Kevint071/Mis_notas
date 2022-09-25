import os
from pyautogui import prompt

lista_archivos_sin_guion = []


def directorio_simple(curso):
    partes_directorio = curso.split("\\")
    videos = os.listdir(curso)

    # Mostrar el nombre de la carpeta

    print("\n" + "_" * 70)
    print(f"\nDirectorio: {partes_directorio[-1]}\n")

    for nombre in videos:
        num = nombre[:2].replace(".", "")

        # Mirar si el archivo de video inicia por un numero

        i = 0

        while i < 10:
            if num.count(str(i)) == False:
                i += 1
            else:

                break

            if i == 10:
                lista_archivos_sin_guion.append(nombre)

        if i == 10:
            continue

        conversion = False

        if num.count("_"):
            return False
            
        # Editar nombre si el archivo de video inicia por 10 o mayor

        elif int(num) > 9:
            conversion = True
            nombre_nuevo = "_" + nombre
            print(" •  " + nombre_nuevo)
            os.rename(nombre, nombre_nuevo)
        else:
            # Pendiente por revision
            if nombre == videos[-1] and conversion == True:
                return True
    return True


def directorio_complejo(directorio_principal):

    cursos = os.listdir(directorio_principal)

    for curso in cursos:
        curso_individual = os.chdir(f"{directorio_principal}/{curso}")
        curso_individual = os.getcwd()
        
        conversion = directorio_simple(curso_individual)

        if conversion == False:
            print("•  Ningun video se convirtió en este directorio...")


def run():

    # Obtener directorio que digite el usuario

    directorio = prompt(text='Digite el directorio al que desea cambiarle los nombres de los archivos', title="Obtener directorio")

    print(directorio)

    directorio_principal = os.chdir(directorio)
    directorio_principal = os.getcwd()
    print(directorio_principal)

    # Ver lo que está dentro de esta carpeta

    directorio_interior = os.listdir(directorio_principal)

    # Mirar si la carpeta tiene subcarpetas o archivos

    print("\nNombres de archivos cambiados: ")

    if directorio_interior[0].count("mp4") >= 1:
        conversion = directorio_simple(directorio_principal)
        if conversion == False:
            print("•  Ningun video convertido en este directorio...")
    else:
        directorio_complejo(directorio_principal)

    # Mostrado archivos que no inician por numero
    
    if len(lista_archivos_sin_guion) > 0:
        print("\n" + "_" * 70)
        print(f'\nERROR... No se pudo agregar guion a algunos archivos:\n')

        for i in lista_archivos_sin_guion:
            print(f" •  {i}")

        print("\nVerifique que los archivos comiencen por numeros")
    
    input("\nPresione enter para salir...")

if __name__ == "__main__":
    run()

