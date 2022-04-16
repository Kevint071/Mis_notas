import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)


def factorial(n):
    """Calcula el factorial de un número

    n > 0 int cualquier numero
    returns factorial de n
    """
    if n == 1:
        return 1
    
    return n * factorial(n-1)

n = int(input("Digite un número: "))

print(f"El factorial de el número {n} es: {factorial(n)}")
