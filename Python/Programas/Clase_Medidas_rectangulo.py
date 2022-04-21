class rectangulo:
    def __init__(self):
        self.base = int(input("Digite la base del rectángulo: "))
        self.altura = int(input("Digite la altura del rectángulo: "))
        print()

    def hallar_area(self):
        print(f"El área del rectángulo es {lados.base * lados.altura}")

    def hallar_perimetro(self):
        print(f"El perimetro del rectángulo es {lados.base * 2 + lados.altura * 2}")
    
lados= rectangulo()
