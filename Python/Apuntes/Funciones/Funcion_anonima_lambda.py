# Funcion lambda que muestre un numero

mostrar_numero = lambda numero: print(f"El número digitado es: {numero}\n")
mostrar_numero(int(input("Digite un numero: ")))

# Funcion lambda que suma dos numeros

sumar = lambda num1, num2: print(f"La suma de {num1} y {num2} es: {num1 + num2}\n")
sumar(int(input('Digite el número 1: ')),int(input('Digite el número 2: ')))

# Otra manera de sumar 2 numeros con la funcion lambda

num1 = int(input("Digite el numero 1: "))
num2 = int(input("Digite el numero 2: "))

sumar = lambda num1, num2: num1 + num2
print(f"La suma de {num1} y {num2} es: {sumar(num1, num2)}")
