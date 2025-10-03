"""
Develop an Object-Oriented (OO) Python project that reads either a string or a
list, then performs two analyses:
1. Calculates the total length.
2. Determines the number of uppercase characters.
The project should be structured with appropriate classes and methods. After 
implementation, use Pylint to analyze and improve the code quality, ensuring 
adherence to Python’s best practices and style guidelines. Share the result 
when you have done
"""

class Reader:
    """ Class for reader object """
    def __init__(self):
        self.stringtext = ''

    def calculate_length(self, text):
        """ Method to calculate length of string """
        self.stringtext = text
        return len(self.stringtext)

    def count_uppercase(self, text):
        """ Method to count the number of uppercase letters """
        self.stringtext = text
        counter = 0

        for char in self.stringtext:
            if char.isupper():
                counter += 1
        return counter

if __name__ == "__main__":
    STRING_TEXT = "Hello World!"
    reader_obj = Reader()

    strlen = reader_obj.calculate_length(STRING_TEXT)
    print(strlen)

    UPPERCASE_COUNT = reader_obj.count_uppercase(STRING_TEXT)
    print(UPPERCASE_COUNT)
