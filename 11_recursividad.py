def fibonacci(n):
    """ Calcula la poblacion de conejas en determinado tiempo.

        param int n meses transcurridos
        returns la cantidad de conejas en determinado mes
    """

    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))