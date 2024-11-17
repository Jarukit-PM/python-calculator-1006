import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    #Add()
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 5), 7)
        self.assertEqual(self.calc.add(4, 6), 10)
    
    #Subtract()
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(9, 4), 5)

    #Multiply()
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 2), 10)

    #Divide()
    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 3), 4)
        self.assertEqual(self.calc.divide(8, 4), 2)

    #Modulo()
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9, 4), 1)
        self.assertEqual(self.calc.modulo(15, 6), 3)
if __name__ == '__main__':
    unittest.main()