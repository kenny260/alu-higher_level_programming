#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry and validates dimensions."""

    def __init__(self, width, height):
        """Initializes the rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
