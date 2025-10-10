"""
Week 10 - Activiy 1
Kristine Gonzalvo
MSE800

Develop an Object-Oriented (OO) Python project that reads either a string or a
list, then performs two analyses:
1. Calculates the total length.
2. Determines the number of uppercase characters.
The project should be structured with appropriate classes and methods. After 
implementation, use Pylint to analyze and improve the code quality, ensuring 
adherence to Python’s best practices and style guidelines. Share the result 
when you have done
"""

class InputAnalyzer:
    """ This is the base class analyzer """
    def __init__(self, data):
        self.data = data

    def total_length(self):
        """ Method/Function placeholder to be implemented by subclass """
        raise NotImplementedError("Subclasses should implement this method.")

    def count_uppercase(self):
        """ Method/Function placeholder to be implemented by subclass """
        raise NotImplementedError("Subclasses should implement this method.")


class StringAnalyzer(InputAnalyzer):
    """ Class for analyzing string input """
    def total_length(self):
        return len(self.data)

    def count_uppercase(self):
        counter = 0
        for char in self.data:
            if char.isupper():
                counter += 1
        return counter


class ListAnalyzer(InputAnalyzer):
    """ Class for analyzing list input"""
    def total_length(self):
        return len(self.data)

    def count_uppercase(self):
        count = 0
        for item in self.data:
            if isinstance(item, str):
                for char in item:
                    if char.isupper():
                        count += 1
        return count


def main():
    """ Function for the main processing """
    # Test with a string
    string_input = "Hello World!"
    string_analyzer = StringAnalyzer(string_input)
    print(f"String input: {string_input}")
    print("Total length:", string_analyzer.total_length())
    print("Uppercase letters:", string_analyzer.count_uppercase())

    print()

    # Test with a list
    list_input = ["Hello", "WORLD", 123, "Python"]
    list_analyzer = ListAnalyzer(list_input)
    print("List input:")
    print(list_input)
    print("Total length:", list_analyzer.total_length())
    print("Uppercase letters:", list_analyzer.count_uppercase())


if __name__ == "__main__":
    main()
