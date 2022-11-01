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
        """ instantiates an instance of class User """
        super().__init__(*args, **kwargs)
