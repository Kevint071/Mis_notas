# Return devuelve un valor especifico dentro de una funcion y hace que la funcion tenga ese valor de acuerdo a los parámetros dados

# Ejemplo 1

def multiplicar(num1, num2):
    print(f"La multiplicacion de {num1} y {num2} es: ", end = "")
    resultado = num1 * num2
    return resultado

multiplicacion_3_6 = multiplicar(3, 6)
print(multiplicacion_3_6)

# Ejemplo 2

def mostrar_mensaje():
    mensaje = "\nHola, este es un mensaje de prueba"
    return mensaje

frase_mensaje = mostrar_mensaje()
print(frase_mensaje)