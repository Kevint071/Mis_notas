# Este codigo solo ordena los archivos del directorio dado, no sus carpetas ni subcarpetas

from os import chdir, listdir, path


def generar_lista_solo_archivos(directorio):
    lista_directorio = listdir(directorio)
    lista_archivos = list(
        map(lambda x: path.join(directorio, x), lista_directorio))
    lista_archivos = list(filter(lambda x: not path.isdir(x), lista_archivos))


def run():
    directorio = input("Digite el directorio a organizar: ")
    chdir(directorio)
    generar_lista_solo_archivos(directorio)


if __name__ == "__main__":
    run()
