class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    def get_grade(self):
        return self.__grade
    
    # add one more method to the class that uses the private attribute
    def set_grade(self, grade):
        self.__grade = grade
        print("New grade set!")

# create a new class to demonstrate the use of the public and protected attributes
class Peer(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

    def greet(self):
        # subclass can access public attribute of parent class
        print(f"Hello from {self.name}")

    def show_details(self):
        # subclass can access protected attribute of parent class
        print(f"John is {self._age} years old")
        # subclass cannot access private attribute of parent class
        #print(f"{self.name}'s grade is {self.__grade}")  # this will not work


s = Student('Ali', 20)
print(s.name)         # accessible
print(s._age)         # discouraged
print(s.get_grade())  # correct way

s.set_grade('B')
print(f"New grade: {s.get_grade()}")

p = Peer('John', 22)
p.greet()
p.show_details()
