import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()
        
    def test_suma_positiva(self):
        self.assertEqual(self.calc.sumar(2,3),8, "deberia ser 5")
        
    def test_suma_negativa(self):
        self.assertEqual(self.calc.sumar(-1,-1),-2, "deberia ser -2")
        
if __name__ == '__main__':
    unittest.main()