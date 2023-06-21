import pyautogui as pyto
from time import sleep

def configuracion_listas_señales():
    tiempos = [5, 15]
    rango_dias = range(2, 12 +1)
    periodos_ema = [9, 21, 50]
    rango_backtesting = range(1, 12 + 1)
    rango_porcentaje = range(70, 100 +1, 3)

    return [tiempos, rango_dias, rango_porcentaje, periodos_ema, rango_backtesting]


def seleccionar_tipo_mercado():
    pyto.press("tab")
    sleep(0.2)
    pyto.press("tab")
    sleep(0.2)
    pyto.press("down")
    pyto.press("down")
    sleep(0.2)
    pyto.press("enter")
    pyto.press("esc")


def seleccionar_martingalas(porcentaje, num):
    pyto.press("tab")

    if num == 0:
        pyto.press("tab")
        pyto.write(str(porcentaje))
    if num == 1:
        pyto.press("down")
        pyto.press("tab")
        pyto.write(str(porcentaje))
        pyto.press("tab")

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
    

def seleccionar_call_put():
    pyto.press("tab")
    pyto.press("down")
    pyto.press("down")


def tiempo_operacion(tiempo):
    pyto.press("tab")

    if tiempo == 5:
        pyto.press("down")
    elif tiempo == 15:
        pyto.press("down")
        pyto.press("down")


def agregar_dias(dia):
    pyto.press("tab")
    pyto.write(str(dia))


def agregar_ema():
    pass
