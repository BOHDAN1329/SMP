import unittest
import Calculator as calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(-7, 2.8), -4.2)
        self.assertEqual(calculator.add(0, -2), -2)
        self.assertEqual(calculator.add(1, 2), 3.0)
        with self.assertRaises(TypeError):
            calculator.add(40, "cat")
            calculator.add("lives", "ice")
            calculator.add("5", "+")

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 2.5), -1.5)
        self.assertEqual(calculator.subtract(0.8, -2), 2.8)
        self.assertEqual(calculator.subtract(-9, -7), -2)
        with self.assertRaises(TypeError):
            calculator.subtract("2", "-")
            calculator.subtract("brown", 5)
            calculator.subtract(3, "+")

    def test_multiply(self):
        self.assertEqual(calculator.multiply(1.5, 3), 4.5)
        self.assertEqual(calculator.multiply(0, -2), 0)
        self.assertEqual(calculator.multiply(-0.5, -2), 1.0)
        with self.assertRaises(TypeError):
            calculator.multiply(3, "+")
            calculator.multiply("2", "-")
            calculator.multiply("log", 5)

    def test_divide(self):
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertEqual(calculator.divide(0, -2), 0)
        self.assertEqual(calculator.divide(-0.5, 2), -0.25)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)
            calculator.divide(0, 0)
        with self.assertRaises(TypeError):
            calculator.divide("d", "+")
            calculator.divide(3, "+")
            calculator.divide("94gs", 9)