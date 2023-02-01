import cv2, datetime, os

cantidad_letras = []

def hallar_tiempo (directorio_video, nombre, peso, x):

    # Funcion que halla el tiempo de el video por medio de un directorio

    x += 1

    datos = cv2.VideoCapture(directorio_video)

    frames = int(datos.get(cv2.CAP_PROP_FRAME_COUNT)) # Fotogramas
    fps = datos.get(cv2.CAP_PROP_FPS) # fps

    seconds = int(frames / fps)
    video_time = str(datetime.timedelta(seconds=seconds))
    datos = f"Duracion del video: {video_time}     Peso: {round(peso, 3)}"

    if x == 1:
        cantidad_letras.append(len(datos))

        
    if int(cantidad_letras[0]) > len(datos):
        espacio = " " * (5 + (cantidad_letras[0] - len(datos)))
    elif int(cantidad_letras[0]) < len(datos):
        espacio = " " * (5 - (len(datos) - cantidad_letras[0]))
    else:
        espacio = " " * 5

    print(f"Duracion del video: {video_time}     Peso: {round(peso, 3)} MB{espacio}Nombre: {nombre}")


def run():

    # Obtener directorio de la carpeta de videos

    directorio = input("Digite el directorio raiz de los videos (carpeta donde se encuentran los videos): ")

    os.chdir(directorio)
    directorio_principal = os.getcwd()

    # Obtener la lista de videos y eliminar archivos de la lista que no sean videos

    lista_videos = os.listdir(directorio_principal)

    for i in lista_videos:
        if i.count(".mp4") == 0:
            print(f"\nArchivo eliminado de la lista: {i}")
            lista_videos.remove(i)

    print("\nLista de los videos...\n")

    lista_videos.sort()

    j = 0

    # Ciclo para hallar la duracion de cada video de la lista de videos

    acum = 0
    x = 0

    for i in lista_videos:
        nombre = i.strip(". ")

        # Hallar directorio de cada video y ver su peso

        directorio_video = f"{directorio_principal}/{i}"
        peso = os.path.getsize(directorio_video) / (1024 ** 2)
        acum += peso

        # Hallar el tiempo de cada video

        hallar_tiempo(directorio_video, nombre, peso, x)
        j += 1
    
    print(f"\nPeso total: {round(acum, 2)} MB")
    
if __name__ == "__main__":
    run()