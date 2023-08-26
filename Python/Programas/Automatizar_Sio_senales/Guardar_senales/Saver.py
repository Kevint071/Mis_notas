import os
from datetime import datetime
from Funciones_saver import ejecutar_navegador, retroceder_a_catalogador, cerrar_anuncio, elegir_idioma, seleccionar_mercado, obtener_inputs, agregar_efectividad, agregar_direccion_op, agregar_timeframe, agregar_dia, filtrar_noticias, iniciar_catalogacion, obtener_senales
from time import time, sleep
from Optimizador_descargas import configuracion_listas_senales
from colorama import Fore, Style


def guardar_senales_txt(nombre_archivo, senales):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(senales)


def obtener_cantidad_senales(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        cantidad_senales = archivo.readlines()
        print(f"Cantidad de señales: {len(cantidad_senales)}")
        return cantidad_senales


def configuracion_catalogador_txt(directorio_sin_filtro, timeframe, tiempos, dia, porcentaje):
    os.chdir(directorio_sin_filtro)

    with open("configuracion_catalogador.txt", "w") as archivo:
        if timeframe == tiempos[0]:
            archivo.write(f"{tiempos}\n")
        elif timeframe == tiempos[1]:
            archivo.write(f"{tiempos[1:]}\n")
        else:
            archivo.write(f"{tiempos[2]}\n")

        archivo.write(f"{dia}\n")
        archivo.write(f"{porcentaje}")


def configurar_catalogacion(timeframe, porcentaje, dia):
    print("Iniciando configuración de catalogación...")
    funciones_catalogacion = [seleccionar_mercado, obtener_inputs, agregar_efectividad, agregar_direccion_op, agregar_timeframe, agregar_dia, filtrar_noticias, iniciar_catalogacion]

    params = {agregar_efectividad: (porcentaje, ),
              agregar_timeframe: (timeframe, ),
              agregar_dia: (dia, ),}

    for funcion in funciones_catalogacion:
        args = params.get(funcion, ())
        funcion(*args)
        sleep(0.1)


def obtener_guardar_senales(directorio):
    # Creando directorio carpeta fecha
    dia_actual, mes_actual = [datetime.now().day, datetime.now().strftime("%B")]
    carpeta_fecha = f"{mes_actual}_day_{dia_actual}"

    os.chdir(directorio)

    if not os.path.exists(carpeta_fecha):
        os.mkdir(carpeta_fecha)

    # Creando directorio carpeta Sin_filtro

    directorio_fecha = os.path.join(directorio, carpeta_fecha)
    os.chdir(directorio_fecha)

    carpeta_senales_sin_filtro = "Sin_filtro"

    if not os.path.exists(carpeta_senales_sin_filtro):
        os.mkdir(carpeta_senales_sin_filtro)

    cantidad_archivos_descargados = 0
    lista_tiempos_catalogacion = []

    directorio_sin_filtro = os.path.join(directorio_fecha, carpeta_senales_sin_filtro)

    rangos = configuracion_listas_senales(directorio_sin_filtro)
    tiempos, rango_dias, rango_porcentaje = rangos
    hora_inicio = datetime.now().strftime("%H:%M:%S")
    print(f"Hora de inicio: {hora_inicio}")

    ejecutar_navegador()
    sleep(0.5)
    cerrar_anuncio()
    sleep(0.5)
    elegir_idioma()

    for timeframe in tiempos:
        
        os.chdir(directorio_sin_filtro)
        carpeta_tiempo = f"Tiempo_M{timeframe}"

        if not os.path.exists(carpeta_tiempo):
            os.mkdir(carpeta_tiempo)

        for dia in rango_dias:
           
            directorio_tiempo = os.path.join(directorio_sin_filtro, carpeta_tiempo)
            carpeta_dia = f"Dia_{dia}"
            os.chdir(directorio_tiempo)

            if not os.path.exists(carpeta_dia):
                os.mkdir(carpeta_dia)

            for porcentaje in rango_porcentaje:
                tiempo_inicio = time()
                print(Fore.LIGHTCYAN_EX + f"Iniciando Descarga N° {cantidad_archivos_descargados+1}" + Style.RESET_ALL)
                # Configurar catalogación para obtener las señales
                configurar_catalogacion(timeframe, porcentaje, dia)

                senales = obtener_senales()
                if senales == None:
                    retroceder_a_catalogador()
                    break
                if (rango_porcentaje != range(72, 100+1, 4) or porcentaje == 100) or senales == None:
                        rango_porcentaje, rango_dias = range(72, 100 + 1, 4), range(2, 12 + 1)
                retroceder_a_catalogador()
                sleep(1)

                # Crear carpeta dia, guardando señales en arhcivos txt

                directorio_dia = os.path.join(directorio_tiempo, carpeta_dia)
                os.chdir(directorio_dia)

                lineas = senales.split("\n")
                num_lineas = len(lineas)
                nombre_archivo = f"Porcentaje_{porcentaje}_tiempo_{timeframe}_sen_{num_lineas}.txt"

                print("Señales obtenidas...\n")
                guardar_senales_txt(nombre_archivo, senales)
                cantidad_archivos_descargados += 1

                print(Fore.CYAN + f"Archivo Número {cantidad_archivos_descargados}" + Style.RESET_ALL)
                print(f"Tiempo_operación: {timeframe} minutos")
                print(f"Día: {dia}")
                print(f"Porcentaje: {porcentaje}")
                print(f"Cantidad de señales: {num_lineas}")

                # obtener_cantidad_senales(nombre_archivo)
                configuracion_catalogador_txt(directorio_sin_filtro, timeframe, tiempos, dia, porcentaje)

                tiempo_fin = time()
                tiempo_catalogacion = round(tiempo_fin - tiempo_inicio, 2)
                lista_tiempos_catalogacion.append(tiempo_catalogacion)
                hora_actual = datetime.now().strftime("%H:%M:%S")

                print(f"Hora de la descarga: {hora_actual}")
                print(f"Tiempo de guardado: {tiempo_catalogacion} s")
                print(
                    f"Tiempo total: {round(sum(lista_tiempos_catalogacion) // 3600):02d}:{round((sum(lista_tiempos_catalogacion) % 3600) // 60):02d}:{round((sum(lista_tiempos_catalogacion)) % 3600 % 60):02d}")
                print(
                    f"Promedio tiempo: {round(sum(lista_tiempos_catalogacion)/len(lista_tiempos_catalogacion), 2)} s\n")


    ruta_archivo_configuracion = os.path.join(directorio_sin_filtro, "configuracion_catalogador.txt")

    if os.path.exists(ruta_archivo_configuracion):
        os.remove(ruta_archivo_configuracion)