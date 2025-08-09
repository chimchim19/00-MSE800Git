##import string

class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def find_string_length(self):
        return len(self.text)
    
    def convert_to_upper_case(self):
        return self.text.upper()

def main():
    # Create an instance of the StringManipulator class
    name = StringManipulator("example")

    # Call the find_character method on the object
    result = name.find_character('x')
    # Output 1
    print(f"Character \'x\' is found at index {result} of the string \'{name.text}\'")

    length_result = name.find_string_length()
    # Output 2
    print(f"The length of the string \'{name.text}\' is {length_result}")

    upper_case = name.convert_to_upper_case()
    # Output 3
    print(f"The string \'{name.text}\' converted to upper case is \'{upper_case}\'")


if __name__ == "__main__":
    main()