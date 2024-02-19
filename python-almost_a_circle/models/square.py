#!/usr/bin/python3
"""
Square model inherited from Rectangle


"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherited from Base
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of the Square class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the Square class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """
        Getter of the size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter of the size attribute
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square class
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Dictionary representation of the Square class
        """
        return {"id": self.id, "x": self.x, "size": self.size,  "y": self.y}
