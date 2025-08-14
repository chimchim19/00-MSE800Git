"""
You are tasked with developing a simple program for the Human Resources (HR) department 
to store and display basic employee information, including each employee's name, 
salary, and job title.
Requirements:
    1. Create at least two Employee objects with different data.
    2. Call the display_info() method to show each employee's details.
    3. Call the give_raise() method to increase an employee's salary and 
        display the updated amount.
"""

class Employee:
    def __init__(self):
        self.name = input("Name: ")
        self.title = input("Job Title: ")
        self.salary = float(input("Salary: "))

    # display employee infomation
    def display_info(self):
        print(f"\nEmployee Name: {self.name}")
        print(f"Job Title: {self.title}")
        # format display to 2 decimal places
        print(f"Salary: {self.salary:.2f} NZD p.a.")
    
    # increase employee salary per input
    def give_raise(self):
        print(f"\nPlease enter salary raise for {self.name}.")
        salary_increase = float(input("Increase salary by: "))
        self.salary += salary_increase
        # format display to 2 decimal places
        print(f"{self.name}'s updated salary is {self.salary:.2f} NZD p.a.")

if __name__ == "__main__":

    print("\nHello, HR team.")
    print("Please enter information of first employee.")
    employee1 = Employee() # instantiate first employee

    print("Please enter information of second employee.")
    employee2 = Employee()  # instantiate second employee

    print("\nThe following details have been stored.")
    employee1.display_info()
    employee2.display_info()

    employee1.give_raise()
    employee2.give_raise()

    print("\nThe employees' details have been updated!")
    employee1.display_info()
    employee2.display_info()
    print("\n  -- E N D --")