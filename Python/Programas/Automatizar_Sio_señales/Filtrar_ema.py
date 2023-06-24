from screeninfo import get_monitors
import pyppeteer
from asyncio import run, sleep
from os import path, makedirs, walk
from pyppeteer_stealth import stealth
from Cataloger import configuracion_listas_señales

periodos_ema = configuracion_listas_señales()[3]
directorio = r"C:\Users\andre\Escritorio\Operaciones_Trading\June_day_11"


async def pegar_obtener_señales(root, nombre_archivo, page):
    # Pegar la ruta actual con el archivo para obtener su contenido
    for periodo in periodos_ema:

        await page.reload()
        await sleep(0.4)

        # Cerrar anuncio
        await page.click(".closeWS")

        lista_rutas_filtradas = []
        lista_rutas_filtradas.clear()

        ruta_archivo = path.join(root, nombre_archivo)
        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.read()

        await sleep(0.2)

        # Obteniendo el textarea de la pagina y pegando las señales del archivo de señales
        textarea = await page.waitForSelector('textarea')
        await textarea.click()
        await sleep(0.1)
        await page.type('textarea', contenido)

        # Agregando el periodo en la pagina

        input_periodo = await page.waitForXPath("//input[@name='period']")
        await input_periodo.click()
        await sleep(0.1)
        await input_periodo.type(str(periodo))
        await sleep(0.1)

        # Dar click al boton para filtrar

        boton_filtrar = await page.waitForXPath('//button[contains(text(), "Filtrar Sinais")]')
        await sleep(0.1)
        await boton_filtrar.click()

        # Obtener señales filtradas
        await sleep(2)
        await page.waitForSelector('textarea')
        señales_filtradas = await page.evaluate('document.querySelector("textarea").value')

        root_filtro = root.replace("Sin_filtro", "Filtro_ema")
        root_filtro =path.join(root_filtro, f"Filtro_{periodo}")
        nombre_archivo_filtrado = nombre_archivo.replace(".txt", "") + f"_filtro_{periodo}" + ".txt"
        
        makedirs(root_filtro, exist_ok=True)
        ruta_archivo_filtrado = path.join(root_filtro, nombre_archivo_filtrado)

        if ruta_archivo_filtrado not in lista_rutas_filtradas:
            print(ruta_archivo_filtrado)
            with open(ruta_archivo_filtrado, "w") as archivo:
                archivo.write(señales_filtradas)
        else:
            print("Ya este archivo está agregado")


async def filtrar_señales_ema(page):
    for root, dirs, archivos in walk(directorio):
        for nombre_archivo in archivos:
            await pegar_obtener_señales(root, nombre_archivo, page)
            await sleep(0.4)


async def main():
    # Iniciar y lanzar nueva ventana
    browser = await pyppeteer.launch(headless=False, executablePath=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe", args=['--start-maximized'])
    page = await browser.newPage()
    await stealth(page)
    await page.goto("https://siofiltrosinais.com/trend")

    # Obtener tamaño de la pantalla para agregarla a la ventana creada
    monitor = get_monitors()[0]
    width = monitor.width
    height = monitor.height
    await page.setViewport({'width': width, 'height': height})

    # Cerrar pagina por defecto si hay una

    pages = await browser.pages()
    if len(pages) > 1:
        await pages[0].close()

    await filtrar_señales_ema(page)

    await browser.close()


if __name__ == "__main__":
    run(main())

