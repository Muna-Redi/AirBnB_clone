#!/usr/bin/env python3
""" Module for class User """

from models.base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from BaseModel

    Attributes:
        email (str): email of the user
        password (str): password for user
        first_name (str): User's first name
        last_name (string): User's  last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ init method for class User 

        Args:
            args (list): list of argument to be initialised to an instnce
            kwargs (dict): keyword arguments to the init method

        """
        super().__init__(args, kwargs)
