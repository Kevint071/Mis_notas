import cv2, datetime, os


def hallar_tiempo (directorio, video, num_video, nombre):

    datos = cv2.VideoCapture(f"{directorio}/{video}")

    frames = int(datos.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = datos.get(cv2.CAP_PROP_FPS)

    seconds = int(frames / fps)
    video_time = str(datetime.timedelta(seconds=seconds)) 

    if num_video <= 9:
        print(f"Duracion del video {num_video}: {video_time}      Nombre: {nombre}")
    else:
        print(f"Duracion del video {num_video}: {video_time}     Nombre: {nombre}")


def run():
    directorio = input("Digite el directorio raiz de los videos (carpeta donde se encuentran los videos): ")

    directorio_principal = os.chdir(directorio)
    directorio_principal = os.getcwd()

    lista_videos = os.listdir(directorio_principal)

    for i in lista_videos:
        if i.count(".mp4") == 0:
            print(f"\nArchivo eliminado de la lista: {i}")
            lista_videos.remove(i)

    print("\nLista de los videos...\n")

    j = 0

    for i in lista_videos:
        num = lista_videos[j][0:3]
        num = int(num.strip(" ._"))
        nombre = i[3:].strip(". ")
        hallar_tiempo(directorio_principal, i, num, nombre)
        j += 1
    
if __name__ == "__main__":
    run()