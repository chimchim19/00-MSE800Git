
class DemoFile:

    def __init__(self, filename):
        self.filename = filename
    
    def read_file(self):
        fileobject = open(self.filename, "r", encoding="UTF-8")
        filecontent = fileobject.read()
        fileobject.close()
        return filecontent
    
    def get_word_count(self, filecontent):
        # divide the string into a list of substrings
        word_list = filecontent.split()
        # len() returns the number of splitted substrings
        return len(word_list)
    

if __name__ == "__main__":
    
    my_demo = DemoFile("Week3/demo.txt")
    
    # read content of the file
    read_content = my_demo.read_file()
    # count the number of words in the file
    number_of_words = my_demo.get_word_count(read_content)
    print("\nFile is read successfully!")
    print(f"There are a total of {number_of_words} words in the demo file.")