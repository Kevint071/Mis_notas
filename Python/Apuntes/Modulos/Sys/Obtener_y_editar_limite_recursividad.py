import sys

# Para  obtener el limite de recursividad se hace lo siguiente

variable = sys.getrecursionlimit()
print(variable) # 1000

# Para editarlo se hace lo siguiente:

sys.setrecursionlimit(1300) # El límite editado que se puso es 1300

# Esto sirve para cuando necesites hacer algo con un límite de recursividad mayor a (el número de recursividad obtenido con sys.getrecursionlimit), ya que python por defecto coloca este número como el límite para que no haya un debordamiento en C y python no se bloquee.