from os import path, chdir, listdir
from sys import path as pth
from Funciones_filtro_ema import ejecutar_navegador, cerrar_anuncio, retroceder_a_filtrador


root = path.dirname(path.dirname(path.abspath(__file__)))
pth.append(root)

from Directorio import obtener_directorio
directorio = obtener_directorio()


def obtener_timeframes(temporalidades):
   timeframes = []
   for i in temporalidades:
      num = i.split("M")[1]
      timeframes.append(int(num))


def main():
    # ejecutar_navegador()
    # cerrar_anuncio()

    dirrectorio_sin_filtro = path.join(directorio, "Sin_filtro")
    chdir(dirrectorio_sin_filtro)
    temporalidades = listdir(dirrectorio_sin_filtro)

    for tiempos in temporalidades:
      print(listdir(tiempos))
    # AQUI COLOCA UN CICLO FOR QUE RECORRA A TIEMPO M15 y TIEMPO M5 PARA PODER OBTENER LOS TXT
    timeframes= obtener_timeframes(temporalidades)
    

if __name__ == "__main__":
  main()










# Crear directorio