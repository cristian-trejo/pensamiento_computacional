import sys

def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    returns n!    
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input('Escribe un entero: '))

print(factorial(n))

# Imprimimos el limite de recursion que trae python por defecto con la funcion sys.getrecursionlimit() que trae el modulo sys. 
print(f'Limite de recursiones en Python: {sys.getrecursionlimit()}')

# Modificamos el limite de recursion a 2000 con la funcion sys.setrecursionlimit() que trae el modulo sys
sys.setrecursionlimit(2000)