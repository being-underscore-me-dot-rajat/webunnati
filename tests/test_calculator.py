import unittest

from calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(5, 2), 3)

    def test_division(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
