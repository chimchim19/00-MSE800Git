""" Week 11 - Activity 1: Unit testing
Develop a test unit for the *, -, / and % functions and add it to the below example. 
Once completed, please push your updated code to GitHub and share it here.
"""
import unittest

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(0, 10), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 8), -6)

    def test_divide(self):
        self.assertEqual(divide(21, 3), 7)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(25, 0)

    def test_modulo(self):
        self.assertEqual(modulo(7, 2), 1)
        self.assertEqual(modulo(15, 4), 3)


if __name__ == "__main__":
    unittest.main()
