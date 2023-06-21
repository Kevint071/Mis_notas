import os, pyautogui as pyto
from Cataloger import configuracion_listas_señales

periodos_ema = configuracion_listas_señales()[3]

directorio = r"C:\Users\andre\Escritorio\Operaciones_Trading\June_day_11"
directorio_archivos_filtrados = []

for periodo in periodos_ema:
    for root, dirs, archivos in os.walk(directorio):
        
        for nombre_archivo in archivos:
            ruta_archivo = os.path.join(root, nombre_archivo)
            with open(ruta_archivo, "r") as archivo:
                contenido = archivo.read()
            
            root_filtro = root.replace("Sin_filtro", "Filtro_ema")
            os.makedirs(root_filtro, exist_ok=True)
            nombre_archivo_filtro = nombre_archivo
            ruta_archivo_filtrado = os.path.join(root_filtro, nombre_archivo)
            print(nombre_archivo_filtro)
           