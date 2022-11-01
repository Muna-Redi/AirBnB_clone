#!/usr/bin/env python3
""" The module for City class """


from models.base_model import BaseModel


class City(BaseModel):
    """ State class inherits from BaseModel

    Attributes:
        state_id (str): holds the state id from state.id
        name (str): city's name
    """
    state_id = ""
    name = ""
