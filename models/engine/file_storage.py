#!/usr/bin/env python3
""" File Storage class """


import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review


class FileStorage:
    """
        this class serializes/deserializes our objects in Json
        for storage and retreival

        Attributes:
            __file_path (str): path to the json file that will store all
            objects

            __objects (dict): dictionary containing all objects with key
            classname.id

        Methods:
            all: returns the the dictionary of all objects
            new: sets a new obj in the dictioinry __objects
            save: serilizes __objects to the json file
            reload
    """
    __file_path = "storage.json"
    __objects = dict()

    def __init__(self):
        """ No initialization required """
        pass

    def all(self):
        """ This method returns the dictionary(__objects) of the class """

        return FileStorage.__objects

    def new(self, obj):
        """
            This method sets a new object in __objects
            Args:
                obj (object): new object to be set in __objects

        """

        """
              getting the key for the dictionary from objects class
             name and uniqued id
        """

        key = "{}.{}".format(obj.to_dict()["__class__"], obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        """
            This method serializes the __objects to the
            __file_path("storage.json")
        """

        new_dictionary = {}
        for key, value in FileStorage.__objects.items():
            new_dictionary[key] = value.to_dict()

        """ opening file in write mode as the file needs to be created if
            it doesn't exist plus contents will be derived from the private
            class attribute __objects each time save is called
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:

            json.dump(new_dictionary, f)

    def reload(self):
        """ This method deserializes the json file (__file_path)
            to __objects
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:

                dictionary = json.load(f)

                """ loading to __objects """

                for key, value in dictionary.items():
                    FileStorage.__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            """" do nothing """
            pass
