from asyncio import run
from os import makedirs
from Saver import obtener_guardar_señales


async def main():
    directorio = r"C:\Users\andre\Escritorio\Operaciones_Trading"
    makedirs(directorio, exist_ok=True)

    await obtener_guardar_señales(directorio)


if __name__ == "__main__":
    run(main())