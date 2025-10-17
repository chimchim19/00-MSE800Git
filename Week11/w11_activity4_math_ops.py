""" Week 11 - Activity 4: Implementing Doctest and Unittest in Python
Update the testing section in Week 11 - Activities 1 & 2 by implementing doctesting or a
combination of unittest and doctest (hybrid testing).
"""
import unittest
import doctest


def add(x, y):
    """
    Add two numbers and return their sum.

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(5, 5)
        10
        >>> add(-5, -3)
        -8
        >>> add(0, 0)
        0
    """
    return x + y


def multiply(x, y):
    """
    Multiply two numbers and return their product.

    Examples:
        >>> multiply(1, 5)
        5
        >>> multiply(2, 5)
        10
        >>> multiply(0, 10)
        0
        >>> multiply(-3, 4)
        -12
        >>> multiply(-2, -5)
        10
    """
    return x * y


def subtract(x, y):
    """
    Subtract y from x and return the result.

    Examples:
        >>> subtract(2, 8)
        -6
        >>> subtract(10, 5)
        5
        >>> subtract(0, 5)
        -5
        >>> subtract(5, 5)
        0
    """
    return x - y


def divide(x, y):
    """
    Divide x by y and return the result.
    Raises ZeroDivisionError if y is zero

    Examples:
        >>> divide(21, 3)
        7.0
        >>> divide(10, 2)
        5.0
        >>> divide(9, 3)
        3.0
        >>> divide(15, 5)
        3.0
        >>> divide(25, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
    """
    return x / y


def modulo(x, y):
    """
    Return the remainder of x divided by y.
    Raises ZeroDivisionError if y is zero

    Examples:
        >>> modulo(7, 2)
        1
        >>> modulo(15, 4)
        3
        >>> modulo(10, 5)
        0
        >>> modulo(20, 3)
        2
        >>> modulo(25, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer modulo by zero
    """
    return x % y


class TestMathOperations(unittest.TestCase):
    """ Test cases for basic mathematical operations """

    def test_add(self):
        """ Test addition with positive and negative numbers """
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(-5, -3), -8)

    def test_multiply(self):
        """ Test multiplication with various numbers """
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(0, 10), 0)

    def test_multiply_with_negative(self):
        """ Test multiplication with negative numbers """
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(-2, -5), 10)

    def test_subtract(self):
        """ Test subtraction with various numbers """
        self.assertEqual(subtract(2, 8), -6)

    def test_subtract_with_negative(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-10, 5), -15)

    def test_divide(self):
        self.assertEqual(divide(21, 3), 7)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(25, 0)

    def test_modulo(self):
        self.assertEqual(modulo(7, 2), 1)
        self.assertEqual(modulo(15, 4), 3)

    def test_modulo_by_zero(self):
        """Test that modulo by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            modulo(25, 0)


if __name__ == "__main__":
    # Run doctests
    print("\nRunning Doctests...\n")
    # verbose=True prints detailed information about each test it runs
    doctest.testmod(verbose=True)

    # Run unit tests
    print("\n" + "="*70)
    """
    By passing argv=[''], this prevents it from trying to interpret command-line args

    verbosity=1 (default): Shows a dot . for each successful test
    verbosity=2: More verbose, shows the name of each test and its status

    exit=False tells unittest.main() not to call sys.exit() after running the tests.
    """
    print("\nRunning Unit Tests...\n")
    unittest.main(argv=[''], verbosity=2, exit=False)
