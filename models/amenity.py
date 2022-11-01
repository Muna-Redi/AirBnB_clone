#!/usr/bin/env python3
""" module for the amenity class """


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class Amenity inherits fro BaseModel

        Attributes:
            name (str): name of Amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initializes an instance of the Amenity class

            Args:
                args (list): list of attributes to be initialised
                to an instance
                kwargs (dict): dictionary of keyword arguments to
                the init method
        """
        super().__init__(*args, **kwargs)
