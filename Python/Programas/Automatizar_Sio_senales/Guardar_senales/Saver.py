import os
from datetime import datetime
from Funciones_saver import ejecutar_navegador, retroceder_a_catalogador, cerrar_anuncio, elegir_idioma, seleccionar_mercado, obtener_inputs, agregar_efectividad, agregar_direccion_op
from time import time, sleep
from Optimizador_descargas import configuracion_listas_senales


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

    # with open("dir_descargas_senales.txt", "w") as archivo:
    #     archivo.write(f"{directorio}")

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
    cerrar_anuncio()
    elegir_idioma()

    for tiempo_op in tiempos:
        # Directorio para crear las carpetas de dias
        os.chdir(directorio_sin_filtro)
        carpeta_tiempo = f"Tiempo_M{tiempo_op}"

        if not os.path.exists(carpeta_tiempo):
            os.mkdir(carpeta_tiempo)

        for dia in rango_dias:
            # Directorio para crear las carpetas de dias
            directorio_tiempo = os.path.join(directorio_sin_filtro, carpeta_tiempo)
            carpeta_dia = f"Dia_{dia}"
            os.chdir(directorio_tiempo)

            if not os.path.exists(carpeta_dia):
                os.mkdir(carpeta_dia)

            for porcentaje in rango_porcentaje:
                tiempo_inicio = time()
                if cantidad_archivos_descargados != 0:
                    retroceder_a_catalogador()
                if porcentaje == 100 and rango_porcentaje != range(72, 100+1, 4):
                    rango_porcentaje, rango_dias = range(72, 100 + 1, 4), range(2, 12 + 1)

                seleccionar_mercado()
                obtener_inputs()
                agregar_efectividad(porcentaje)
                agregar_direccion_op()

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
                
                sleep(100)



    ruta_archivo_configuracion = os.path.join(directorio_sin_filtro, "configuracion_catalogador.txt")

    if os.path.exists(ruta_archivo_configuracion):
        os.remove(ruta_archivo_configuracion)

    print("\nDescarga de señales finalizada exitosamente...")