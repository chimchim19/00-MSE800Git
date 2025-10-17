""" Week 11 - Activity 4: Implementing Doctest and Unittest in Python
Update the testing section in Week 11 - Activities 1 & 2 by implementing doctesting or a
combination of unittest and doctest (hybrid testing).
"""
import unittest
import doctest


class Expense:
    """
    Class to represent a single expense entry.

    Examples:
        >>> exp = Expense("Coffee", 5.50)
        >>> exp.description
        'Coffee'
        >>> exp.amount
        5.5
        >>> exp.amount > 0
        True

        >>> Expense("Lunch", -10.00)
        Traceback (most recent call last):
            ...
        ValueError: Amount cannot be negative

        >>> Expense("", 20.00)
        Traceback (most recent call last):
            ...
        ValueError: Description must be a non-empty string
    """
    
    def __init__(self, description: str, amount: float):
        """
        Initialize an Expense object.
        description: Description of the expense
        amount: Amount spent (must be positive)
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if not description or not isinstance(description, str):
            raise ValueError("Description must be a non-empty string")

        self.description = description
        self.amount = amount


class ExpenseTracker:
    """
    Manages a collection of expenses with methods to add and calculate totals.

    Examples:
        >>> tracker = ExpenseTracker()
        >>> tracker.get_expense_count()
        0

        >>> tracker.add_expense("Coffee", 5.50)
        >>> tracker.get_expense_count()
        1

        >>> tracker.add_expense("Lunch", 15.00)
        >>> tracker.calculate_total_expense()
        20.5

        >>> tracker.calculate_total_expense() > 0
        True

        >>> len(tracker.get_all_expenses())
        2

        >>> tracker.clear_expenses()
        >>> tracker.get_expense_count()
        0

        >>> tracker.add_expense("Book", 0.00)
        >>> tracker.calculate_total_expense()
        0.0

        >>> tracker.add_expense("Invalid", -5.00)
        Traceback (most recent call last):
            ...
        ValueError: Amount cannot be negative
    """

    def __init__(self):
        """Initialize an empty ExpenseTracker."""
        self.expenses = []

    def add_expense(self, description: str, amount: float):
        """
        Add a new expense to the tracker.

        Example:
            >>> tracker = ExpenseTracker()
            >>> tracker.add_expense("Gas", 40.00)
            >>> tracker.get_expense_count()
            1
        """
        expense = Expense(description, amount)
        self.expenses.append(expense)

    def calculate_total_expense(self):
        """
        Calculate the total of all expenses.

        Example:
            >>> tracker = ExpenseTracker()
            >>> tracker.add_expense("Item1", 10.00)
            >>> tracker.add_expense("Item2", 20.00)
            >>> tracker.calculate_total_expense()
            30.0
        """
        return sum(expense.amount for expense in self.expenses)

    def get_all_expenses(self):
        """
        Retrieve all recorded expenses.

        Example:
            >>> tracker = ExpenseTracker()
            >>> tracker.add_expense("Coffee", 5.00)
            >>> expenses = tracker.get_all_expenses()
            >>> len(expenses)
            1
        """
        return self.expenses.copy()

    def get_expense_count(self):
        """
        Get the number of expenses recorded.

        Example:
            >>> tracker = ExpenseTracker()
            >>> tracker.get_expense_count()
            0
            >>> tracker.add_expense("Item", 10.00)
            >>> tracker.get_expense_count()
            1
        """
        return len(self.expenses)

    def clear_expenses(self) -> None:
        """
        Clear all expenses from the tracker.

        Example:
            >>> tracker = ExpenseTracker()
            >>> tracker.add_expense("Item", 10.00)
            >>> tracker.get_expense_count()
            1
            >>> tracker.clear_expenses()
            >>> tracker.get_expense_count()
            0
        """
        self.expenses.clear()


# Unit Tests
class TestExpense(unittest.TestCase):
    """ Test cases for the Expense class """

    def test_expense_creation(self):
        """ Test creating a valid expense """
        expense = Expense("Lunch", 15.50)
        self.assertEqual(expense.description, "Lunch")
        self.assertEqual(expense.amount, 15.50)

    def test_expense_negative_amount(self):
        """ Test that negative amounts raise ValueError """
        with self.assertRaises(ValueError) as context:
            Expense("Invalid", -10.00)
        self.assertIn("negative", str(context.exception))

    def test_expense_zero_amount(self):
        """ Test that zero amount is valid """
        expense = Expense("Free item", 0.00)
        self.assertEqual(expense.amount, 0.00)

    def test_expense_empty_description(self):
        """ Test that empty description raises ValueError """
        with self.assertRaises(ValueError):
            Expense("", 20.00)

    def test_expense_invalid_description_type(self):
        """ Test that non-string description raises ValueError """
        with self.assertRaises(ValueError):
            Expense(123, 20.00)


class TestExpenseTracker(unittest.TestCase):
    """ Test cases for the ExpenseTracker class """

    def setUp(self):
        """ Initialize a fresh tracker for each test """
        self.tracker = ExpenseTracker()

    def test_add_single_expense(self):
        """ Test adding a single expense """
        self.tracker.add_expense("Coffee", 5.00)
        self.assertEqual(self.tracker.get_expense_count(), 1)

    def test_add_multiple_expenses(self):
        """ Test adding multiple expenses """
        self.tracker.add_expense("Coffee", 5.00)
        self.tracker.add_expense("Lunch", 15.00)
        self.tracker.add_expense("Gas", 40.00)
        self.assertEqual(self.tracker.get_expense_count(), 3)

    def test_calculate_total_expense_empty(self):
        """ Test calculating total with no expenses """
        self.assertEqual(self.tracker.calculate_total_expense(), 0.00)

    def test_calculate_total_expense_single(self):
        """ Test calculating total with one expense """
        self.tracker.add_expense("Book", 12.99)
        self.assertEqual(self.tracker.calculate_total_expense(), 12.99)

    def test_calculate_total_expense_multiple(self):
        """ Test calculating total with multiple expenses """
        self.tracker.add_expense("Coffee", 5.00)
        self.tracker.add_expense("Lunch", 15.50)
        self.tracker.add_expense("Gas", 40.00)
        self.assertAlmostEqual(self.tracker.calculate_total_expense(), 60.50)

    def test_get_all_expenses(self):
        """ Test retrieving all expenses """
        self.tracker.add_expense("Item1", 10.00)
        self.tracker.add_expense("Item2", 20.00)
        expenses = self.tracker.get_all_expenses()
        self.assertEqual(len(expenses), 2)

    def test_clear_expenses(self):
        """ Test clearing all expenses """
        self.tracker.add_expense("Item1", 10.00)
        self.tracker.add_expense("Item2", 20.00)
        self.tracker.clear_expenses()
        self.assertEqual(self.tracker.get_expense_count(), 0)
        self.assertEqual(self.tracker.calculate_total_expense(), 0.00)

    def test_add_expense_with_invalid_input(self):
        """ Test that invalid inputs raise ValueError """
        with self.assertRaises(ValueError):
            self.tracker.add_expense("Item", -5.00)


def display_tracker_summary(tracker: ExpenseTracker):
    """ Display a summary of all expenses in the tracker """
    expenses = tracker.get_all_expenses()

    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpense Tracker Summary\n")
    for index, expense in enumerate(expenses, 1):
        print(f"{index}. {expense.description:<20} ${expense.amount:>8.2f}")
    print("-"*50)
    print(f"{'TOTAL':<20} ${tracker.calculate_total_expense():>8.2f}")
    print("-"*50 + "\n")


if __name__ == "__main__":
    # Run doctests
    print("\nRunning Doctests...\n")
    # verbose=True prints detailed information about each test it runs
    doctest.testmod(verbose=True)

    # Run unit tests
    print("\n" + "="*70)
    print("\nRunning Unit Tests...\n")
    """
    By passing argv=[''], this prevents it from trying to interpret command-line args

    verbosity=1 (default): Shows a dot . for each successful test
    verbosity=2: More verbose, shows the name of each test and its status

    exit=False tells unittest.main() not to call sys.exit() after running the tests.
    """
    unittest.main(argv=[''], verbosity=2, exit=False)

    tracker = ExpenseTracker()

    # Add some sample expenses
    tracker.add_expense("Coffee", 5.50)
    tracker.add_expense("Lunch at Restaurant", 25.75)
    tracker.add_expense("Groceries", 45.30)
    tracker.add_expense("Movie Ticket", 15.00)

    display_tracker_summary(tracker)
