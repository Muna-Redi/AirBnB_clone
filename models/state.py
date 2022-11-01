#!/usr/bin/env python3
""" The module for state class """


from models.base_model import BaseModel


class State(BaseModel):
    """ State class inherits from BaseModel

    Attributes:
        name (str): state's name
    """
    name = ""
