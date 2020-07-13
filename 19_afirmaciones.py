# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es str'
            assert len(palabra) > 0, 'No se permiten str vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras

lista = ['Python', 192, '', '13aB', 3.1416]
print(primera_letra(lista))