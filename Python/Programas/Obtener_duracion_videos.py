import cv2, datetime, os


def hallar_tiempo (directorio, video, num_video, nombre):

    # Funcion que halla el tiempo de el video por medio de un directorio

    datos = cv2.VideoCapture(f"{directorio}/{video}")

    frames = int(datos.get(cv2.CAP_PROP_FRAME_COUNT)) # Fotogramas
    fps = datos.get(cv2.CAP_PROP_FPS) # fps

    seconds = int(frames / fps)
    video_time = str(datetime.timedelta(seconds=seconds)) 

    if num_video <= 9:
        print(f"Duracion del video {num_video}: {video_time}      Nombre: {nombre}")
    else:
        print(f"Duracion del video {num_video}: {video_time}     Nombre: {nombre}")


def run():

    # Obtener directorio de la carpeta de videos

    directorio = input("Digite el directorio raiz de los videos (carpeta donde se encuentran los videos): ")

    directorio_principal = os.chdir(directorio)
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

    for i in lista_videos:
        num = lista_videos[j][0:3]
        num = int(num.strip(" ._"))
        nombre = i[3:].strip(". ")
        hallar_tiempo(directorio_principal, i, num, nombre)
        j += 1
    
if __name__ == "__main__":
    run()