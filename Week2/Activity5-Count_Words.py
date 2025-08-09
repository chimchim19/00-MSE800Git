import string

class StringManipulator:
    def __init__(self):
        # initialize the object asking input from the user
        self.statement = input("Please write one sentence.:")
        self.number_of_words = 0

    def count_words(self):
        # split() function splits the string by separator. If no separator mentioned, default split is by whitespaces found
        # len() function will get the length or number of splitted words
        return len(self.statement.split())

def start():
    sentence = StringManipulator()

    # call the method to count the words
    sentence.number_of_words = sentence.count_words()

    # print the count of words found
    print(f"This sentence contains {sentence.number_of_words} word(s).")

if __name__ == "__main__":
    start()