import time

def enumeracionExhaustiva(objetivo):
    start_time = time.time()            
    respuesta = 0
    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'Elegiste el metodo Exhaustivo.\nLa raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')
    print('Tiempo de ejecucion: %s segundos' % (time.time() - start_time))

def aproximacion(objetivo):
    start_time = time.time()    
    epsilon = 0.01        
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and  respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo >= epsilon):

        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'Elegiste el metodo de Aproximacion.\nLa raiz cuadrada de {objetivo} es {respuesta}')
    print('Tiempo de ejecucion: %s segundos' % (time.time() - start_time))

def busquedaBinaria(objetivo):
    start_time = time.time()    
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
        print(f'Elegiste el metodo de Busqueda Binaria.\nLa raiz cuadrada de {objetivo} es {respuesta}')
    print('Tiempo de ejecucion: %s segundos' % (time.time() - start_time))

def calcularRaiz():
    objetivo  = int(input('Escoge un entero: '))
    algoritmo = int(input('Elige el algoritmo de calculo:\n 1- Enumeracion Exhaustiva\n 2- Aproximacion\n 3- Busqueda Binaria \n'))
    if algoritmo == 1:
        enumeracionExhaustiva(objetivo)
    elif algoritmo == 2:
        aproximacion(objetivo)
    elif algoritmo == 3:
        busquedaBinaria(objetivo)
    else:
        print('Opcion invalida')

calcularRaiz()