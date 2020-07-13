import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class cajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)
        
        # (valor, valorQuerido) = valor == valorQuerido (Nos devuelve un true o false)
        self.assertEqual(resultado, 15)

        #  (valor, valorQuerido) = valor > valorQuerido (Nos devuelve un true o false)
        self.assertGreater(resultado, 14)

        #  (valor, valorQuerido) = valor >= valorQuerido (Nos devuelve un true o false)
        self.assertGreaterEqual(resultado, 15)

        #  (valor, valorQuerido) = valor < valorQuerido (Nos devuelve un true o false)
        self.assertLess(resultado, 16)

        #  (valor, valorQuerido) = valor <= valorQuerido (Nos devuelve un true o false)    
        self.assertLessEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

# si el nombre del modulo (__name__) == al modulo principal (__main__)
if __name__ == '__main__':
    unittest.main()    