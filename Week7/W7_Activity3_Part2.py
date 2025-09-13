"""
Week 7 Activity 3 (Part 2): Design Pattern - Factory
Compare the attached codes from Week 7 Activity 3 (Parts 1 and 2) and explain your understanding in your own code. 
Share both your result and explanation along with a GitHub link.
"""

'''
Answer:
This code demonstrates how with the Factory Design Pattern, we can easily add new shapes without modifying existing factory code.
In part 1, the factory had to be updated as well to handle the new shape type (Triangle). 
Each time a new shape is added, the factory code needs to be changed as well.
In part 2, the factory is using a registry method to map shape types to their classes. This allows new shapes to be 
registered dynamically without changing the factory logic.
'''


from abc import ABC, abstractmethod

# 1) Abstract Product
class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        """Render the shape and return a description."""
        pass


# 2) Concrete Products
class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a Circle"


class Square(Shape):
    def draw(self) -> str:
        return "Drawing a Square"


# This class is added to demonstrate extensibility by adding a new shape without modifying factory code
class Triangle(Shape):
    def draw(self) -> str:
        return "Drawing a Triangle"


# 3) Factory
class ShapeFactory:
    _registry = {
        "circle": Circle,
        "square": Square,
    }

    @classmethod
    def register(cls, name: str, shape_cls: type[Shape]) -> None:
        """Optionally register new shapes without modifying factory code."""
        if not issubclass(shape_cls, Shape):
            raise TypeError("Registered class must inherit from Shape")
        cls._registry[name.lower()] = shape_cls

    @classmethod
    def create(cls, shape_type: str) -> Shape:
        shape_cls = cls._registry.get(shape_type.lower())
        if shape_cls is None:
            raise ValueError(f"Unknown shape type: {shape_type!r}. "
                             f"Available: {', '.join(cls._registry)}")
        return shape_cls()


# 4) Client code (examples)
if __name__ == "__main__":
    factory = ShapeFactory

    circle = factory.create("circle")
    print(circle.draw())  

    square = factory.create("square")
    print(square.draw())

    # creating a new shape without modifying factory code
    ShapeFactory.register("triangle", Triangle) # this registers the new shape class Triangle
    triangle = factory.create("triangle") # now we can create a Triangle instance
    print(triangle.draw())
