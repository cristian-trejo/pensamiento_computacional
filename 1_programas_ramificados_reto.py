nombre_usuario_1 = input('Ingresa tu nombre: ')
nombre_usuario_2 = input('Ingresa tu nombre: ')

edad_usuario_1 = int(input('Escribe tu edad ' + nombre_usuario_1 + ': '))
edad_usuario_2 = int(input('Escribe tu edad ' + nombre_usuario_2 + ': '))

if edad_usuario_1 > edad_usuario_2:
    print (f'{nombre_usuario_1} es mayor que {nombre_usuario_2}')
elif edad_usuario_1 < edad_usuario_2:
    print (f'{nombre_usuario_2} es mayor que {nombre_usuario_1}')
else:
    print (f'{nombre_usuario_1} y {nombre_usuario_2} tienen la misma edad')