## Re-write the class by removing the constructor __init__

class StringManipulator:
#    def __init__(self, text):
#        self.text = text

    def find_character(self, stringtext, char):
        #need to receive the string as a parameter/argument if object is without attribute text
        return stringtext.find(char)
    
    def find_string_length(self, stringtext):
        #need to receive the string as a parameter/argument if object is without attribute text
        return len(stringtext)
    
    def convert_to_upper_case(self, stringtext):
        #need to receive the string as a parameter/argument if object is without attribute text
        return stringtext.upper()

def main():
    # Create an instance of the StringManipulator class
    name = StringManipulator()

    name_text = 'example'

    # Call the find_character method on the object
    result = name.find_character(name_text,'x')
    # Output 1
    print(f"Character \'x\' is found at index {result} of the string \'{name_text}\'")

    length_result = name.find_string_length(name_text)
    # Output 2
    print(f"The length of the string \'{name_text}\' is {length_result}")

    upper_case = name.convert_to_upper_case(name_text)
    # Output 3
    print(f"The string \'{name_text}\' converted to upper case is \'{upper_case}\'")


if __name__ == "__main__":
    main()