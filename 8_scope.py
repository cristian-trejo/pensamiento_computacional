x = 'Esta es una variable global'

def funcion():
    x = 'Esta es una variable local'
    global y
    y = 'Esta es una variable global creada desde una funcion'
    print(x)

    def funcion_interior():
        print(f'Imprimiendo desde funcion interior: {x}')        
    funcion_interior()

    #global x
    x = 'Cambiamos el valor de la variable global x'

funcion()
print(x)
print(y)
