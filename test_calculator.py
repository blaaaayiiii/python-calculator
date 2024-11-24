import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(100, -50), 50)
        self.assertEqual(self.calc.add(-100, 50), -50)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-10, -5), -5)
        self.assertEqual(self.calc.subtract(10, 20), -10)

    def test_multiply(self):

        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 10), -10)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(100, 10), 10)
        self.assertEqual(self.calc.divide(-100, -10), 10)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(20, 5), 0)
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(-10, 3), -1)
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
