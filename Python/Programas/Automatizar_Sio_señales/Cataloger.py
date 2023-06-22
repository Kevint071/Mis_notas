import pyautogui as pyto
from asyncio import sleep


def configuracion_listas_señales():
    tiempos = [5, 15]
    rango_dias = range(2, 12 +1)
    periodos_ema = [9, 21, 50]
    rango_backtesting = range(1, 12 + 1)
    rango_porcentaje = range(70, 100 +1, 3)

    return [tiempos, rango_dias, rango_porcentaje, periodos_ema, rango_backtesting]


async def seleccionar_tipo_mercado(page):
    await page.keyboard.press("Tab")
    await sleep(0.2)
    await page.keyboard.press("Tab")
    await sleep(0.2)
    await page.keyboard.press("ArrowDown")
    await sleep(0.1)
    await page.keyboard.press("ArrowDown")
    await sleep(0.2)
    await page.keyboard.press("Enter")
    await sleep(0.2)
    await page.keyboard.press("Escape")


async def seleccionar_martingalas(page, porcentaje, input, num):
    if num == 0:
        await input.click()
        await sleep(0.2)
        await input.type(str(porcentaje))
    if num == 1:
        await page.keyboard.press("ArrowDown")
        await sleep(0.2)
        await page.keyboard.press("Tab")
        await sleep(0.1)
        pyto.write(str(porcentaje))
        await sleep(0.1)
        await page.keyboard.press("Tab")
        

        if porcentaje <= 94:
            pyto.write(str(porcentaje + 5))
        else:
            pyto.write("100")

    if num == 2:
        pyto.press("down")
        pyto.press("down")
        pyto.press("tab")
        pyto.write(str(porcentaje))
        pyto.press("tab")

        if porcentaje <= 89:
            pyto.write(str(porcentaje + 10))
        else:
            pyto.write("100")
        
        if porcentaje + 10 <= 89:
            pyto.write(str(porcentaje + 10))
        else:
            pyto.write("100")
    

async def seleccionar_call_put(page):
    await page.keyboard.press("Tab")
    await sleep(0.1)
    await page.keyboard.press("ArrowDown")
    await sleep(0.1)
    await page.keyboard.press("ArrowDown")
    await sleep(0.1)


async def tiempo_operacion(page, tiempo):
    await page.keyboard.press("Tab")
    await sleep(0.1)

    if tiempo == 5:
        await page.keyboard.press("ArrowDown")
    elif tiempo == 15:
        await page.keyboard.press("ArrowDown")
        await sleep(0.1)
        await page.keyboard.press("ArrowDown")


async def agregar_dias(page, dia, input):
    await page.keyboard.press("Tab")
    await input.click()
    await sleep(0.2)
    await input.type(str(dia))

