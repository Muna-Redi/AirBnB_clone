#!/usr/bin/env python3

"""
    Module for class BaseModel
"""


from datetime import datetime
import uuid
import models


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
    def __init__(self, *args, **kwargs):
        """
            initializes a new instance with required attribute of the class
            args:
                args (list): list of arguments

                kwargs (dict): a key word arguments corresponding to the
                    class attributes and their values
        """
        if kwargs is not None and (len(kwargs) > 0):
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    hold = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[key] = hold

                elif key == "id":
                    self.id = value
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ str method for class BaseModel"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ saves the instance of the class """  
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary of all keys and values od __dict__ of
            the instance
        """
        new_dict = self.__dict__.copy()

        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
