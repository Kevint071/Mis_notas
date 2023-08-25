from asyncio import run
from os import makedirs, path
from Saver import obtener_guardar_senales
import sys

root = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(root)

from Directorio import obtener_directorio


def main():
    directorio = obtener_directorio()
    makedirs(directorio, exist_ok=True)

    obtener_guardar_senales(directorio)


if __name__ == "__main__":
    main()
