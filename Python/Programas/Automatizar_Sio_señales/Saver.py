import asyncio
import pyppeteer
import os
from datetime import datetime
from pyppeteer_stealth import stealth
from screeninfo import get_monitors
from Cataloger import configuracion_listas_señales, agregar_dias, seleccionar_call_put, seleccionar_martingalas, seleccionar_tipo_mercado, tiempo_operacion


rangos = configuracion_listas_señales()
tiempos, rango_dias, rango_porcentaje = rangos[:3]
# headless=False, executablePath=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe", args=['--start-maximized']

async def obtener_guardar_señales(directorio):
    # Iniciar y lanzar nueva ventana
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    await stealth(page)
    await page.goto("https://siofiltrosinais.com/cataloger")

    # Obtener tamaño de la pantalla para agregarla a la ventana creada
    monitor = get_monitors()[0]
    width = monitor.width
    height = monitor.height
    await page.setViewport({'width': width, 'height': height})

    await asyncio.sleep(1)

    pages = await browser.pages()
    if len(pages) > 1:
        await pages[0].close()
    
    await asyncio.sleep(0.5)

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

    for tiempo in tiempos:
        # Directorio para crear las carpetas de dias
        directorio_sin_filtro = os.path.join(
            directorio_fecha, carpeta_señales_sin_filtro)
        os.chdir(directorio_sin_filtro)
        carpeta_tiempo = f"Tiempo_M{tiempo}"

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

                await page.reload()
                await asyncio.sleep(0.3)

                # Cerrar anuncio
                await page.click(".closeWS")
                await asyncio.sleep(0.4)
                await page.mouse.click(40, 300)

                # Llenar formulario de Catalogador

                await asyncio.sleep(0.4)
                await seleccionar_tipo_mercado(page)

                inputs = await page.xpath("//input[@type='number']")

                if len(inputs) == 2:
                    input_efectividad, input_dia = inputs
                else:
                    print("Ya no hay 2 elementos inputs")
                    return "No hay 2 inputs"

                await asyncio.sleep(0.4)
                await seleccionar_martingalas(page, porcentaje, input_efectividad, num=0)

                await asyncio.sleep(0.4)
                await seleccionar_call_put(page)

                await asyncio.sleep(0.4)
                await tiempo_operacion(page, tiempo)

                await asyncio.sleep(0.4)
                await agregar_dias(page, dia, input_dia)

                await asyncio.sleep(0.4)

                await page.click("#filter")

                # Enviar el formulario y obtener el textarea con las señales

                await page.waitForXPath('//button[contains(text(), "Catalogar")]')

                catalogar_button = await page.xpath('//button[contains(text(), "Catalogar")]')
                await catalogar_button[0].click()

                await page.waitForSelector('textarea')
                contenido = await page.evaluate('document.querySelector("textarea").value')
                await asyncio.sleep(0.1)

                # Guardar las señales en un bloc de notas

                directorio_dia = os.path.join(directorio_tiempo, carpeta_dia)
                os.chdir(directorio_dia)

                nombre_archivo = f"Porcentaje_{porcentaje}_tiempo_{tiempo}.txt"
                
                print(f"{directorio_dia}")
                print(f"{nombre_archivo}\n")
                print(f"{contenido}\n\n")

                if contenido:
                    with open(nombre_archivo, "w") as archivo:
                        archivo.write(contenido)
                else:
                    break

    await browser.close()
