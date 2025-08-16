
class DemoFile:

    def __init__(self, filename):
        self.filename = filename
    
    def read_file(self):
        fileobject = open(self.filename, "r", encoding="UTF-8")
        filecontent = fileobject.read()
        fileobject.close()
        return filecontent
    
    def write_to_file(self, new_content):
        fileobject = open(self.filename, "w", encoding="UTF-8")
        fileobject.write(new_content)
        fileobject.close()
        print("\nNew content is written to the file successfully.")

    def append_to_file(self, new_content):
        fileobject = open(self.filename, "a", encoding="UTF-8")
        fileobject.write(new_content)
        fileobject.close()
        print("\nNew content is appended to the file successfully.")


if __name__ == "__main__":
    
    my_demo = DemoFile("Week3/demo_fileprocessing.txt")
    
    # read content of the file
    read_content = my_demo.read_file()
    print("\nThe content of this file is as follows:\n")
    print(read_content)
    print("\nFile is read successfully!")

    # write new content to the file, overwriting the file
    my_demo.write_to_file("This line overwrites the file as a new content.\nThis is another line.")
    # append new content to the existing content of the file
    my_demo.append_to_file("\nThis is a new line appended to the file.\nThis ends this demo.")

    # read again the file with its latest content
    read_content = my_demo.read_file()
    print("\nThe new content of this file is as follows:\n")
    print(read_content)
    print("\nFile with new content is read successfully!")
