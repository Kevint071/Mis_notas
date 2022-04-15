# Round se usa para aproximar un valor de un numero flotante a su valor más cercano

print("Round sin parámetros:\n")

num = 1.49
num = round(num)
print(num) # 1

num = 1.5
num = round(num)
print(num) # 2

# Round también se puede utilizar sin variables

print(round(3.2)) # 3
print(round(3.87)) # 4

# Además round acepta un parámetro que es el que delimita la cantidad de decimales que puede haber

print("\nRound con parámetros:\n")

print(round(343.365, 1)) # 343.4
print(round(343.365, 2)) # 343.37
print(round(343.365, 3)) # 343.365