import random
from pyautogui import press
from time import sleep

sleep(3)

lista = []

cantidad_l = random.randint(20, 35)

for i in range(cantidad_l):
    num = random.randint(20, 70)

    press("i", num)
    press("l")

print(f"La cantidad de l es: {cantidad_l}")

