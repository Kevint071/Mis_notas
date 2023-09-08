from os import path, listdir, makedirs
from sys import path as pth

root = path.dirname(path.dirname(path.abspath(__file__)))
pth.append(root)

from Directorio import obtener_directorio


def obtener_archivos(directorio):

    directorio_filtro_ema = path.join(directorio, "Filtro_ema")
    lista_archivos_emas = []
    
    emas = listdir(directorio_filtro_ema)
    print(emas)

    dict_archivos = {}
    
    for ema in emas:
        archivos_por_tiempo = {}
        directorio_tiempo = path.join(directorio_filtro_ema, ema)
        tiempos = listdir(directorio_tiempo)
        lista_archivos_ema = []
        for tiempo in tiempos:
            directorio_dia = path.join(directorio_tiempo, tiempo)
            dias = listdir(directorio_dia)
            archivos_por_dias = {}
            for dia in dias:
                directorio_archivo = path.join(directorio_dia, dia)
                archivos = listdir(directorio_archivo)
                lista_archivos = []
                directorio_confluencias = path.join(directorio, "Confluencias", tiempo, dia)
                makedirs(directorio_confluencias, exist_ok=True)
                for archivo in archivos:

                    with open(path.join(directorio_archivo, archivo), "r") as file_ema:
                        contenido = file_ema.read()
                    with open(path.join(directorio_confluencias, archivo), "w") as file_conf:
                        file_conf.write(contenido)
                    lista_archivos_ema.append(archivo)
                    lista_archivos.append(archivo)
                archivos_por_dias[dia] = lista_archivos
            archivos_por_tiempo[tiempo] = archivos_por_dias
        dict_archivos[ema] = archivos_por_tiempo
        lista_archivos_emas.append(lista_archivos_ema)
    print(dict_archivos)
    return dict_archivos, lista_archivos_emas


def confluenciar_archivos(dict_archivos):
    for ema, tiempos in dict_archivos.items():
        for tiempo, dias in tiempos.items():
            for dia, archivos in dias.items():
                for archivo in archivos:
                    pass



def run():
    directorio = obtener_directorio()
    if directorio == None:
        return None

    dict_archivos = obtener_archivos(directorio)
    # confluenciar_archivos(dict_archivos)




if __name__ == "__main__":
    run()