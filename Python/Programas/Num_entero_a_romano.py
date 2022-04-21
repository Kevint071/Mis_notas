dicc_num_romanos = {   
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}
num = int(input("Digite un numero entre el 1 y el 3999: "))

numero_romano = []

residuo = num

for entero, romano in dicc_num_romanos.items():
    # En la primera iteracion residuo es num. De mas de 1 iteracion residuo es lo que queda de la division
    if residuo >= entero:
        cociente = residuo // entero
        residuo = residuo % entero

        repeticion_romano = cociente * romano
        numero_romano.append(repeticion_romano)

numero_romano = "".join(numero_romano)

print(f"\nEl numero {num} en número romano es: {numero_romano}")

