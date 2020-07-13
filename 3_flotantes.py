x = 0.0 
for i in range(10):
    x += 0.1

if x == 1.0:
    print (f'x = {x}')
else:
    print(f'x != {x}')

# no puede dar el 1.0 ya que no hay suficientes bits para representarlo
# (float) 0.33333333 * 3 = 0.9999999999 por lo que se hacerna a 1.0 y se puede tomar como este    