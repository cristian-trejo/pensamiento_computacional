import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return False
    else:
        return False
        
class pruebaDeCristalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)

# inicializar el codigo, si el nombre de este modulo es == __main__
if __name__ == '__main__':
    # dentro del modulo unittest
    unittest.main(verbosity=2)
    """ verbosity options:
    0 (quiet): you just get the total numbers of tests executed and the global result
    1 (default): you get the same plus a dot for every successful test or a F for every failure
    2 (verbose): you get the help string of every test and the result
    """