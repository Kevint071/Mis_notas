import asyncio
import pyppeteer
import os
from datetime import datetime
from pyppeteer_stealth import stealth
from Cataloger import configuracion_listas_señales, agregar_dias, seleccionar_call_put, seleccionar_martingalas, seleccionar_tipo_mercado, tiempo_operacion
from time import time


async def obtener_guardar_señales(directorio):
    # Iniciar y lanzar nueva ventana
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    page.setDefaultNavigationTimeout(45000)
    await stealth(page)
    await page.goto("https://siofiltrosinais.com/cataloger")
    
    pages = await browser.pages()
    if len(pages) > 1:
        await pages[0].close()
    
    await asyncio.sleep(0.3)

    # Creando directorio carpeta fecha
    dia_actual, mes_actual = [
        datetime.now().day, datetime.now().strftime("%B")]
    carpeta_fecha = f"{mes_actual}_day_{dia_actual}"

    os.chdir(directorio)

    if not os.path.exists(carpeta_fecha):
        os.mkdir(carpeta_fecha)

    # Creando directorio carpeta Sin_filtro
    directorio_fecha = os.path.join(directorio, carpeta_fecha)
    os.chdir(directorio_fecha)
    carpeta_señales_sin_filtro = "Sin_filtro"

    if not os.path.exists(carpeta_señales_sin_filtro):
        os.mkdir(carpeta_señales_sin_filtro)

    cantidad_archivos_descargados = 0
    lista_tiempos_catalogacion = []

    directorio_sin_filtro = os.path.join(directorio_fecha, carpeta_señales_sin_filtro)

    rangos = configuracion_listas_señales(directorio_sin_filtro)
    tiempos, rango_dias, rango_porcentaje = rangos[:3]

    for tiempo_op in tiempos:
        # Directorio para crear las carpetas de dias
        os.chdir(directorio_sin_filtro)
        carpeta_tiempo = f"Tiempo_M{tiempo_op}"

        if not os.path.exists(carpeta_tiempo):
            os.mkdir(carpeta_tiempo)

        for dia in rango_dias:
            # Directorio para crear las carpetas de dias
            directorio_tiempo = os.path.join(
                directorio_sin_filtro, carpeta_tiempo)
            carpeta_dia = f"Dia_{dia}"
            os.chdir(directorio_tiempo)

            if not os.path.exists(carpeta_dia):
                os.mkdir(carpeta_dia)

            for porcentaje in rango_porcentaje:
                tiempo_inicio = time()
                if cantidad_archivos_descargados != 0:
                    print("Recargando página")
                    await page.reload()
                if porcentaje == 100 and rango_porcentaje != range(72, 100+1, 4):
                    rango_porcentaje, rango_dias = range(72, 100 +1, 4), range(2, 12 +1)

                while True:
                    try:
                    # Cerrar anuncio
                        print("Cerrando anuncio")
                        await page.waitForSelector(".closeWS")
                        await page.click(".closeWS")
                        await asyncio.sleep(0.4)
                        await page.mouse.click(40, 300)
                        break
                    except pyppeteer.errors.ElementHandleError:
                        print("No se obtuvo el div para cerrar el anuncio")
                        await page.goto("https://siofiltrosinais.com/cataloger")
                        await asyncio.sleep(1)

                # Obtener los inputs de efectividad y dia para llenarlos
                
                await page.waitForXPath("//input[@type='number']")
                inputs = await page.xpath("//input[@type='number']")

                print("Obteniendo inputs...")
                if len(inputs) == 2:
                    input_efectividad, input_dia = inputs
                else:
                    print("Ya no hay 2 elementos inputs")
                    return "No hay 2 inputs"

                # Llenar formulario de Catalogador

                print("Seleccionando mercado...")
                await asyncio.sleep(0.4)
                await seleccionar_tipo_mercado(page)
                
                print("Agregando porcentaje efectividad...")
                await asyncio.sleep(0.4)
                await seleccionar_martingalas(page, porcentaje, input_efectividad, num=0)

                print("Añadiendo direcciones call y put...")
                await asyncio.sleep(0.4)
                await seleccionar_call_put(page)

                print("Colocando tiempo de operación...")
                await asyncio.sleep(0.4)
                await tiempo_operacion(page, tiempo_op)

                print("Agregando día...")
                await asyncio.sleep(0.4)
                await agregar_dias(page, dia, input_dia)
                await asyncio.sleep(0.4)
                await page.click("#filter")

                # Enviar el formulario

                await page.waitForXPath('//button[contains(text(), "Catalogar")]')

                catalogar_button = await page.xpath('//button[contains(text(), "Catalogar")]')
                await catalogar_button[0].click()
                await asyncio.sleep(2)
                print("El formulario se envió...")

                # Obtener el h1 del loading

                while True:
                    h1 = await page.querySelectorAll("h1")

                    if len(h1) == 2:
                        print("Hay 2 elementos h1...")
                        h1_1 = h1[1]
                        await asyncio.sleep(0.7)
                        contenido_h1 = await page.evaluate('(element) => element.textContent', h1_1)
                    else:
                        print("Hay 1 solo elemento h1...")
                        break

                    if contenido_h1.count("false"):
                        print("Hay un false en el h1")
                        break
                    print("Repetir bucle")
                    await asyncio.sleep(0.1)

                if contenido_h1.count("false"):
                    print("Error false%, recargando pagina...")
                    await page.reload()
                    await asyncio.sleep(2)
                    continue

                # Obtener el textarea con las señales

                print("Obteniendo textarea")
                await page.waitForSelector('textarea')
                contenido = await page.evaluate('document.querySelector("textarea").value')
                print("Textarea obtenido...")
                await asyncio.sleep(0.2)

                # Guardar las señales en un bloc de notas

                directorio_dia = os.path.join(directorio_tiempo, carpeta_dia)
                os.chdir(directorio_dia)

                nombre_archivo = f"Porcentaje_{porcentaje}_tiempo_{tiempo_op}.txt"

                if contenido:
                    print("Señales obtenidas...\n")
                    with open(nombre_archivo, "w") as archivo:
                        archivo.write(contenido)
                        cantidad_archivos_descargados += 1
                        print(
                            f"Archivo Número {cantidad_archivos_descargados}")

                    with open(nombre_archivo, "r") as archivo:
                        cantidad_señales = archivo.readlines()
                    
                    os.chdir(directorio_sin_filtro)

                    with open("configuracion_catalogador.txt", "w") as archivo:
                        if tiempo_op == tiempos[0]:
                            archivo.write(f"{tiempos}\n")
                        elif tiempo_op == tiempos[1]:
                            archivo.write(f"{tiempos[1:]}\n")
                        else:
                            archivo.write(f"{tiempos[2]}\n")

                        archivo.write(f"{dia}\n")
                        archivo.write(f"{porcentaje}")
                else:
                    rango_porcentaje, rango_dias = range(72, 100 +1, 4), range(2, 12 +1)
                    await asyncio.sleep(0.3)
                    break

                
                await asyncio.sleep(0.1)

                print(f"Tiempo_operación: {tiempo_op}")
                print(f"Día: {dia}")
                print(f"Porcentaje: {porcentaje}")
                print(f"Cantidad señales: {len(cantidad_señales)}")

                tiempo_fin = time()
                tiempo_catalogacion = round(tiempo_fin - tiempo_inicio, 2)
                lista_tiempos_catalogacion.append(tiempo_catalogacion)

                print(f"Tiempo de guardado: {tiempo_catalogacion}")
                print(
                    f"Tiempo total: {round(sum(lista_tiempos_catalogacion) // 3600):02d}:{round((sum(lista_tiempos_catalogacion) % 3600) // 60):02d}:{round((sum(lista_tiempos_catalogacion)) % 3600 % 60):02d}")
                print(
                    f"Promedio tiempo: {round(sum(lista_tiempos_catalogacion)/len(lista_tiempos_catalogacion), 2)}\n")
                
                await asyncio.sleep(0.1)
    
    ruta_archivo_configuracion = os.path.join(directorio_sin_filtro, "configuracion_catalogador.txt")
    if os.path.exists(ruta_archivo_configuracion):
        os.remove(ruta_archivo_configuracion)
    await browser.close()
