import unittest
from Cod_Tdd import soma


class TestSoma(unittest.TestCase):
    
    def test_soma_numeros_positivos(self):
        resultado = soma(1, 2)

        self.assertEqual(resultado, 3)

    def test_soma_numeros_negativos(self):
        resultado = soma(1, -1)
        self.assertEqual(resultado, 0)


if __name__ == '__main__':

    unittest.main()