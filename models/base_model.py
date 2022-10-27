#!/usr/bin/env python3

"""
    Module for class BaseModel
"""


from datetime import datetime
import uuid


class BaseModel:
    """ Base class from which other classes inherit from

        attributes:
            id (str): unique id of an instance of the class
            created_at (str): time instance of the class was created
            updated_at (str): time the instance was updated

        methods:
            __str__: prints a string representation of an instance
            of the class
            save: updates the public instance attribute up_dated with
            the current datetime
            to_dict: returns a dictionary representation of the object
    """
    def __init__(self):
        """
            initializes a new instance with required attribute of the class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ str method for class BaseModel"""

        print("[{}] ({}) {}".format(self.__class__.__name__, self.id,
              self.__dict__))

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary of all keys and values od __dict__ of
            the instance
        """
        new_dict = self.__dict__.copy()

        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
