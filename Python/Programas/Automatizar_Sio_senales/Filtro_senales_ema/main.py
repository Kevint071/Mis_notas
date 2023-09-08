from os import path, chdir, remove, makedirs
from sys import path as pth
from colorama import Fore, Style
from Funciones_filtro_ema import ejecutar_navegador, cerrar_anuncio, obtener_senales_txt, agregar_senales_textarea, agregar_periodo, iniciar_filtrado, obtener_senales_filtradas, retroceder_a_filtrador, limpiar_pantalla

root = path.dirname(path.dirname(path.abspath(__file__)))
pth.append(root)

from Directorio import obtener_directorio

def guardar_senales_filtradas(directorio_filtro_ema, ema, tiempo, dia, archivo, senales_filtradas):
    chdir(directorio_filtro_ema)

    ruta_completa = path.join(directorio_filtro_ema, f"Ema_{ema}", tiempo, dia)
    makedirs(ruta_completa, exist_ok=True)

    # Obtener la cantidad de señales filtradas

    lineas = senales_filtradas.split("\n")
    num_lineas = len(lineas)

    archivo = archivo.split("_sen_")
    senales_antes_filtrado = archivo[1].split(".txt")[0]
    archivo = f'{archivo[0]}_sen_{str(num_lineas)}.txt'
    print(f"Señales validadas: {num_lineas} de {senales_antes_filtrado}\n")

    # Abrir archivo en ruta completa para escribir 

    ruta_archivo = path.join(ruta_completa, archivo)
    with open(ruta_archivo, "w") as f:
        f.write(senales_filtradas)
    
def guardar_progreso(directorio_filtro_ema, archivo):
    chdir(directorio_filtro_ema)

    with open("progreso.txt", "a") as progreso:
        progreso.write(f"{archivo}\n")


def comienzo_filtracion(directorio, directorio_filtro_ema, ema):
    directorio_filtro_riesgo = path.join(directorio, "Filtro_riesgo")
    makedirs(directorio_filtro_ema, exist_ok=True)
    chdir(directorio_filtro_ema)

    # Guardar progreso de filtro de ema

    with open("progreso_ema.txt", "w") as progreso:
        if ema == None:
            print(Fore.LIGHTRED_EX + "No se puede agregar la ema porque tiene un valor None..." + Style.RESET_ALL)
        else:
            progreso.write(ema)
    limpiar_pantalla()

    # Pedir continuar (si quedo incompleta la filtracion)

    if path.exists("progreso.txt"):
        while True:
            continuar = int(input("""¿Quiere continuar por donde quedó?:

    1. Sí
    2. No
                                
    Elija una opción (1 o 2): """))
            if continuar in [1, 2]:
                limpiar_pantalla()
                break
            else:
                limpiar_pantalla()
                print("Ese valor no es valido, escriba 1 o 2...\n")
                
    else:
        continuar = None
        
    # Ejecutando navegador
    chdir(directorio_filtro_riesgo)
    ejecutar_navegador()
    cerrar_anuncio()

    # Obtener señales.txt de la carpeta de señales Sin_filtro

    diccionario_archivos, archivos_todos = obtener_senales_txt(directorio_filtro_riesgo)
    archivos_todos = set(i.strip() for i in archivos_todos)

    # Obtener solo los archivos que un no se han filtrado

    if continuar == 1:
        chdir(directorio_filtro_ema)
        with open("progreso.txt", "r") as progreso:
            # cantidad_archivos_filtrados = len(progreso.readlines())
            archivos_filtrados = set(line.strip() for line in progreso)
            cantidad_archivos_filtrados = len(archivos_filtrados)
            print(f"Archivos filtrados: {cantidad_archivos_filtrados}")
        
        archivos_sin_filtrar = archivos_todos - archivos_filtrados
        print(f"Todos los archivos: {len(archivos_todos)}")
        print(f"Archivos para filtrar: {len(archivos_sin_filtrar)}\n")
    else:
        archivos_sin_filtrar = archivos_todos
        cantidad_archivos_filtrados = 0
        print(f"Archivos para filtrar: {len(archivos_todos)}")

    for tiempo, dias in diccionario_archivos.items():
        for dia, archivos in dias.items():
            for archivo in archivos:
                if archivo in archivos_sin_filtrar:
                    ruta_archivo = path.join(tiempo, dia, archivo)
                    ruta = path.join(directorio_filtro_riesgo, ruta_archivo)

                    with open(ruta, "r") as f:
                        contenido = f.read()
                    
                    print(Fore.LIGHTCYAN_EX + f"Archivo N° {cantidad_archivos_filtrados+1}\n" + Style.RESET_ALL)
                    print(f"EMA: {ema}")
                    print(f"Timeframe: {tiempo.split('_')[1]}")
                    print(f"Dia {dia.split('_')[1]}")
                    print(f"Archivo: {archivo}\n")

                    agregar_senales_textarea(contenido)
                    agregar_periodo(ema)
                    iniciar_filtrado()
                    senales_filtradas = obtener_senales_filtradas()
                    retroceder_a_filtrador()
                    if senales_filtradas != None and senales_filtradas != False:
                        guardar_senales_filtradas(directorio_filtro_ema, ema, tiempo, dia, archivo, senales_filtradas)
                    guardar_progreso(directorio_filtro_ema, archivo)
                    cantidad_archivos_filtrados += 1

    chdir(directorio_filtro_ema)

    # Pedir continuar (si quedo incompleta la filtracion)

    if path.exists("progreso.txt"):
        remove("progreso.txt")


def leer_progreso_ema():
    if path.exists("progreso_ema.txt"):
        with open("progreso_ema.txt", "r") as archivo:
            ema_actual = str(archivo.readline())
            print(type(ema_actual), ema_actual)
        return ema_actual
    else:
        return None


def run():
    directorio = obtener_directorio()
    if directorio == None:
        return None
    
    directorio_filtro_ema = path.join(directorio, "Filtro_ema")
    makedirs(directorio_filtro_ema, exist_ok=True)
    chdir(directorio_filtro_ema)
    ema_actual = leer_progreso_ema()
        
    if ema_actual == "10" or ema_actual == None:
        emas = ("10", "21")
    elif ema_actual == "21":
        emas = ("21",)
    else:
        print("Hay un error al agregar emas...\n")

    
    for ema in emas:
        comienzo_filtracion(directorio, directorio_filtro_ema, ema)
    print(Fore.LIGHTYELLOW_EX + "Señales filtradas exitosamente..." + Style.RESET_ALL)
    chdir(directorio_filtro_ema)
    
    if path.exists("progreso_ema.txt"):
        remove("progreso_ema.txt")


if __name__ == "__main__":
    run()