# Return devuelve un valor especifico dentro de una funcion y hace que la funcion tenga ese valor

def multiplicar(num1, num2):
    print(f"La multiplicacion de {num1} y {num2} es: ", end = "")
    resultado = num1 * num2
    return resultado

multiplicacion_3_6 = multiplicar(3, 6)
print(multiplicacion_3_6)