#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
It also includes the necessary BaseGeometry class as per the task requirements.
"""

class BaseGeometry:
    """
    A base class for geometric shapes.
    Provides basic functionality like area calculation and integer validation.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        This method is not implemented in the base class and should be
        overridden by subclasses.

        Raises:
            Exception: Always raises an exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is an integer and greater than 0.

        Args:
            name (str): The name of the value (e.g., "width", "height").
            value (int): The value to be validated.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate width and height using the integer_validator from BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Private instance attributes
        self.__width = width
        self.__height = height

    # The area() method is not required for this specific task (8-rectangle.py)
    # as per the provided 8-main.py test case.
    # The __str__() method is also not explicitly required to return a specific
    # format for this task, as the print(r) output is the default object representation.


        
