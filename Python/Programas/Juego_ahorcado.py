from requests import get
from os import name, system
from unidecode import unidecode


def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "nt" or name == "dos" or name == "ce":
        system("cls")


def quitar_acentos(palabra):
    palabra_sin_acentos = list(unidecode(palabra))

    for indice, letra in enumerate(palabra):
        if letra == "ñ":
            palabra_sin_acentos[indice] = letra
    
    return "".join(palabra_sin_acentos)
        


def adivinar_palabra(palabra):
    intentos = 6
    palabra_guion = ["_"] * len(palabra)
    palabra_sin_acentos = quitar_acentos(palabra)
    letras_atinadas = []
    letras_no_atinadas = []

    aviso = """REGLAS: 
    
    • SE OBTENDRA SOLAMENTE LA PRIMERA LETRA QUE DIGITES
    • ESCRIBE LETRAS SIN ACENTO EXCEPTO LA 'Ñ'""".center(60)

    print(aviso)

    while intentos >= 1:
        if palabra_guion.count("_") >= 1:
            while True:
              print(f"\nDescubre esta palabra: {' '.join(palabra_guion)}")
              letra_atinar = input("Digita una letra: ")
              letra_atinar = letra_atinar.lower()

              if letra_atinar and letra_atinar[0] == "ñ":
                letra_atinar = letra_atinar[0]
                break
              elif letra_atinar:
                letra_atinar = unidecode(letra_atinar[0].lower())
                break
              else:
                print("No dejes el espacio vacío")
                

            if letra_atinar in palabra_sin_acentos and letra_atinar not in letras_atinadas and letra_atinar not in letras_no_atinadas:

                letras_atinadas.append(letra_atinar)

                for indice, letra in enumerate(palabra):
                    if unidecode(letra) in letras_atinadas or (letra == "ñ" and letra in letras_atinadas):
                        palabra_guion[indice] = letra


            elif letra_atinar not in palabra_sin_acentos and letra_atinar not in letras_no_atinadas:
                letras_no_atinadas.append(letra_atinar)
                intentos -= 1
                print(f"\nEsa letra no va, te quedan {intentos} intentos")
            elif letra_atinar in letras_atinadas:
                print("Esta letra ya la agregaste, intenta otra")
            elif letra_atinar in letras_no_atinadas:
                print("Ya intentaste con esta prueba otra")
        else:
            print(f"Haz descubierto la palabra '{palabra}'! ")
            return True
    if intentos == 0:
        print(f"Perdiste, la palabra era {palabra}")
    return False


def obtener_palabra():
    url = "https://clientes.api.greenborn.com.ar/public-random-word"
    response = get(url)

    if response.status_code == 200:
        data = response.json()[0].lower()
        return data
    else:
        return "Error, no se pudo obtener la palabra"


def run():
    while True:
        limpiar_pantalla()
        palabra = obtener_palabra()
        adivinar_palabra(palabra)
        jugar = int(input("\n¿Quieres volverlo a intentar? 1(si) 2(no): "))

        if jugar == 2:
            break


if __name__ == "__main__":
    run()
