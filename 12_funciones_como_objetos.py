
# Argumentos de otras funciones
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(operacion, numeros):
    resultados = []
    for numero in numeros:
        resultado = operacion(numero)
        # append añade un elemento al final de la lista
        resultados.append(resultado)
    return resultados

areglo_numeros = [1, 2, 3]
print(f'Calculo recibiendo Argumentos de otros funciones: {aplicar_operacion(sumar_dos, areglo_numeros)}')

# Funciones en expresiones
sumar = lambda x, y: x + y
print(f'Calculo con Expresiones (keyword -> lambda <vars>: <expresion>): {sumar(2, 3)}')

# Funciones en Estructuras de datos
def aplicar_operaciones(num):
    operaciones = [abs, float]
    
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

print(f'Calculo con Funciones utlizando estructura de datos: {aplicar_operaciones(-2)}')
