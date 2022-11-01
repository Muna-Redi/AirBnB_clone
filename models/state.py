#!/usr/bin/env python3
""" The module for state class """


from models.base_model import BaseModel


class State(BaseModel):
    """ State class inherits from BaseModel

    Attributes:
        name (str): state's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialises an instance of class State

        Args:
            args (list): list of arguments to be initialised to an instance
            kwargs (dict): keyworad arguments to the __init__ method
        """
        super.__init__(args, kwargs)
