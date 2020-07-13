estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

# bucle for directamente en el diccionario, esto permite iterar
# a lo largo de las llaves del diccionario
for pais in estudiantes:
    print (pais)

# bucle for en la llamada keys del diccionario, lo cual nos
# permite iterar a lo largo de las llaves del diccionario
for pais in estudiantes.keys():
    print (pais)

# bucle for en la llamada values del diccionario, lo cual
# nos permite iterar a lo largo de los valores del diccionario
for numero_de_estudiantes in estudiantes.values():
    print (numero_de_estudiantes)

# bucle for en la llamada items del diccionario, lo cual
# nos permite iterar en una tupla las llaves y los valores del diccionario 
for pais, numero_de_estudiantes in estudiantes.items():
    print (pais, numero_de_estudiantes)

matriz = [[1,2,3], [4,5,6], [7,8,9]]
for fila in matriz:
    for elemento in fila:
        print(elemento)

# Ejecutar en la consola
frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)
# El iterador guarda el estado interno de la iteracion, de tal manera
# que cada llamada sucesiva a next regresa el siguiente elemento
next(iterador)