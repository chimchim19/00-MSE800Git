"""
Week 10 - Activity 2: Extend your Activity W10 - A1 - Pylint
Kristine Gonzalvo
MSE800

Enhance your existing project by extending its functionality to count digits and special
characters within the given input text or string.
Ensure that the updated project maintains a clear and well-structured object-oriented design,
incorporating appropriate classes, methods, and documentation.
 
After completing the implementation, run Pylint to evaluate your code quality and make necessary
improvements to ensure full compliance with Python’s best practices and style guidelines.
Finally, share your results and Pylint report once the task is complete.
"""


import string

class InputAnalyzer:
    """
    A base class for analyzing various types of input data (string or list).
    Defines abstract methods for calculating total length, counting uppercase,
    digits, and special characters.
    """
    def __init__(self, data):
        """
        Initializes the input data.

        Parameters:
            data (str | list): The input data (either a string or a list of items).
        """
        self.data = data

    def total_length(self):
        """
        Calculates the total length of the input data.
        
        Returns:
            int: Length of the data.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def count_uppercase(self):
        """
        Counts the number of uppercase characters in the input data.
        
        Returns:
            int: Number of uppercase characters.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def count_digits(self):
        """
        Counts the number of digits in the input data.
        
        Returns:
            int: Number of digits.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def count_special_characters(self):
        """
        Counts the number of special characters in the input data.
        
        Returns:
            int: Number of special characters.
        """
        raise NotImplementedError("Subclasses should implement this method.")


class StringAnalyzer(InputAnalyzer):
    """
    Analyzes string data, providing methods to calculate total length,
    count uppercase characters, digits, and special characters.
    """
    def total_length(self):
        """ Returns the length of the string. """
        return len(self.data)

    def count_uppercase(self):
        """ Returns the count of uppercase letters in the string. """
        count = 0
        for char in self.data:
            if char.isupper():
                count += 1
        return count

    def count_digits(self):
        """ Returns the count of digits in the string. """
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count

    def count_special_characters(self):
        """
        Returns the count of special characters in the string.
        Special characters are considered any non-alphanumeric character.
        """
        count = 0
        for char in self.data:
            if char in string.punctuation:
                count += 1
        return count


class ListAnalyzer(InputAnalyzer):
    """
    Analyzes list data, where each element can be a string or other types.
    Provides methods to calculate total length, count uppercase characters,
    digits, and special characters.
    """
    def total_length(self):
        """ Returns the total number of elements in the list. """
        return len(self.data)

    def count_uppercase(self):
        """ Returns the count of uppercase letters in string elements of the list. """
        count = 0
        for item in self.data:
            if isinstance(item, str):
                for char in item:
                    if char.isupper():
                        count += 1
        return count

    def count_digits(self):
        """ Returns the count of digits in string elements of the list. """
        count = 0
        for item in self.data:
            if isinstance(item, str):
                for char in item:
                    if char.isdigit():
                        count += 1
        return count

    def count_special_characters(self):
        """ Returns the count of special characters in string elements of the list. """
        count = 0
        for item in self.data:
            if isinstance(item, str):
                for char in item:
                    if char in string.punctuation:
                        count += 1
        return count


def main():
    """ Function for the main processing """
    # Test with a string
    string_input = "Hello World! 123"
    string_analyzer = StringAnalyzer(string_input)
    print("String input analysis:")
    print(string_input)
    print("Total length:", string_analyzer.total_length())
    print("Uppercase letters:", string_analyzer.count_uppercase())
    print("Digits:", string_analyzer.count_digits())
    print("Special characters:", string_analyzer.count_special_characters())

    print()

    # Test with a list
    list_input = ["Hello", "WORLD123!", 456, "Python@3"]
    list_analyzer = ListAnalyzer(list_input)
    print("List input analysis:")
    print(list_input)
    print("Total length:", list_analyzer.total_length())
    print("Uppercase letters:", list_analyzer.count_uppercase())
    print("Digits:", list_analyzer.count_digits())
    print("Special characters:", list_analyzer.count_special_characters())


if __name__ == "__main__":
    main()
