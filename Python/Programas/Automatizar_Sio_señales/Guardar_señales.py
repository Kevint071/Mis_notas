import asyncio, os
from Saver import obtener_guardar_señales


async def main():
    directorio = r"C:\Users\andre\Escritorio\Operaciones_Trading"

    if not os.path.exists(directorio):
        os.mkdir(directorio)

    await obtener_guardar_señales(directorio)

if __name__ == "__main__":
    asyncio.run(main())