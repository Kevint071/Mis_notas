from os import system, name, path


def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "nt" or name == "dos" or name == "ce":
        system("cls")


def continuar_descarga_senales():
    usar_conf = int(input("""¿Deseas seguir descargando señales por donde quedaste?
        
    1. Si
    2. No
        
    Elige un número: """))

    return usar_conf


def elegir_tiempo_op ():
    tiempos = []

    opciones_tiempos = {
        1: 1,
        2: 5,
        3: 15,
        4: (1, 5),
        5: (1, 15),
        6: (5, 15),
        7: (1, 5, 15)
    }

    while True:
        elegir_tiempos = int(input("""Tiempo de operacion de las señales:
                
    1. Operaciones de 1 Minuto
    2. Operaciones de 5 Minutos
    3. Operaciones de 15 Minutos
    4. Operaciones de 1 y 5 Minutos
    5. Operaciones de 1 y 15 Minutos
    6. Operaciones de 5 y 15 Minutos
    7. Operaciones de 1, 5 y 15 Minutos
            
    Elige una opcion: """))

        if elegir_tiempos in opciones_tiempos:
            tiempos.extend(opciones_tiempos[elegir_tiempos])
            limpiar_pantalla()
            break
        else:
            print("Opcion no válida")
    return tiempos


def obtener_archivo_configuracion_listas_senales(ruta_archivo_configuracion):
    with open(ruta_archivo_configuracion, 'r') as archivo:
        lineas = archivo.readlines()
        tiempos = [int(x) for x in lineas[0].strip("[]\n").split(", ")]
        rango_dias = range(int(lineas[1]), 12 +1)
        rango_porcentaje = range(int(lineas[2]), 100 + 1, 4)

    return [tiempos, rango_dias, rango_porcentaje]


def configuracion_listas_senales(directorio_sin_filtro):
    limpiar_pantalla()

    ruta_archivo_configuracion = path.join(directorio_sin_filtro, "configuracion_catalogador.txt")

    while True:
        if path.exists(ruta_archivo_configuracion):
            usar_conf = continuar_descarga_senales()
            limpiar_pantalla()
            
            if usar_conf == 1:
                return obtener_archivo_configuracion_listas_senales(ruta_archivo_configuracion)
            elif usar_conf == 2:
                break
            else:
                print("Opcion no válida")
        else:
            rango_dias = range(2, 12 + 1)
            rango_porcentaje = range(72, 100 + 1, 4)
            tiempos = elegir_tiempo_op()

            return [tiempos, rango_dias, rango_porcentaje]