import unittest
from simple_calculator import SimpleCalculator


class test(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, 3), 2)
        self.assertEqual(self.calc.add(-1.2, 20.2), 19.0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(-1, 20), -21)
        self.assertEqual(self.calc.subtract(1, 5), -4)
        self.assertEqual(self.calc.subtract(5, 1), 4)
        self.assertEqual(self.calc.subtract(1, -1), 0)
        self.assertEqual(self.calc.subtract(2.2, 1.2), 1.0)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
        self.assertEqual(self.calc.multiply(-1, 2), -2)
        self.assertEqual(self.calc.multiply(-2, -2), 4)
        self.assertEqual(self.calc.multiply(0, 12), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    def test_division(self):
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-6, -3), 2)

