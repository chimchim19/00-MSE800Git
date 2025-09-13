"""
Week 7 Activity 3: Design Pattern - Factory
What problems might arise if a program directly creates objects with in multiple places instead of using a Factory class? 
See teh attached code. Share the GitHub link with your description.
"""

# To create a new object of a specific type, the client code must know the exact class name and how to instantiate it.
# In this case, the factory class had to be updated as weell to handle the new shape type.
# This creates tight coupling between the client code and the concrete classes, making it harder to change or extend the code later.

class Circle: # Concrete class
    def draw(self):
        return "Drawing a Circle"

class Square: # Concrete class
    def draw(self):
        return "Drawing a Square"
    
# added a concrete class Triangle to demonstrate the issue when the factory is not updated.
class Triangle:
    def draw(self):
        return "Drawing a Triangle"

class ShapeFactory: # Factory class
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
        # added handling for triangle to show the factory can be updated
        if shape_type == "triangle":
            return Triangle()
        else:
            return None

# this is the client code:
factory = ShapeFactory()
shape = factory.create_shape("triangle")   
# print(shape)  # Output: None before the code was updated to hande triangle
print(shape.draw())  # This will raise an AttributeError (before the code was updated)
                     # since shape is None
                     # shape_type == "triangle" is not handled in the factory
