class Person:
    def __init__(self, name, address, age, id):
        self.name = name
        self.address = address
        self.age = age
        self.id = id

# Staff (subclass) inherits from Person (superclass)
class Staff(Person):
    def __init__(self, name, address, age, id, code, rate):
        
        # calls super() to initialize inherited attributes from parent class
        super().__init__(name, address, age, id)

        # initialize child class' own attributes
        self.taxcode = code
        self.payrate = rate

if __name__ == "__main__":

    person1 = Person("Tom", "123 Apple Street", 35, 1005)
    staff1 = Staff("Ana", "55 Sunrise Blvd", 25, 1008, "M", 45)

    # object typed reference to superclass
    print(f"{person1.name}, age {person1.age}, lives at {person1.address}")

    # object typed reference to subclass
    print(f"{staff1.name}, age {staff1.age}, lives at {staff1.address}")
    print(f"{staff1.name} has tax code {staff1.taxcode} at {staff1.payrate} hourly pay rate")
    