#!/usr/bin/env python3
""" Tests for the the Base class """


from datetime import datetime
import inspect
import pep8
import unittest

import models
from models import base_model
BaseModel = base_model.BaseModel


class Test_BaseModel_Doc(unittest.TestCase):
    """ Tests class for the Base Model doc strings"""

    def test_base_model_pep8_conformance(self):
        """ Tests for pep8style conformance of the base model module """
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(["models/base_model.py"])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style error (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        """ Tests for pep8style conformance of the test_base_model"""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(["tests/test_models/test_base_model.py"])
        self.assertEqual(outcome.total_errors, 1,
                         "Found code style error (and warnings).")

    def test_base_model_docstring(self):
        """ tests if the base_model module has a documentation """
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_BaseModel_docstring(self):
        """ tests if the BaseModel class docstring is present """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_BaseModel_methods_docstring(self):
        """ tests if the methods in the class are documented """

        bm = inspect.getmembers(BaseModel, inspect.isfunction)
        for method in bm:
            if method[1]:
                self.assertTrue(len(method[1].__doc__) >= 1)


class TestBaseModel(unittest.TestCase):
    """ Class to test the BaseModel class """

    def setUp(self):
        """Set up method for object obj of BaseModel"""
        self.obj = BaseModel()

    def tearDown(self):
        """cleans the slate for new test"""
        self.obj = None

    def test_isClass(self):
        """ test BaseModel """

        self.assertIsInstance(self.obj, BaseModel)
        self.assertEqual(type(self.obj), BaseModel)

    def test_basic_attribute_set(self):
        """ test for basic attributes of BaseModel instances """
        self.obj.first_name = 'Muna'
        self.obj.last_name = 'Israel'
        self.assertEqual(self.obj.first_name, 'Muna')
        self.assertEqual(self.obj.last_name, 'Israel')

    def test_str(self):
        """ tests str method """
        string = str(self.obj)
        objid = "[{}] ({}) {}".format(self.obj.__class__.__name__, self.obj.id,
                                      self.obj.__dict__)
        test = objid in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime" in string
        self.assertEqual(True, test)

    def test_to_dict(self):
        """ tests to_dict method """
        my_dict = self.obj.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.obj.created_at.isoformat())
        self.assertEqual(datetime, type(self.obj.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.obj.__class__.__name__)
        self.assertEqual(my_dict['id'], self.obj.id)

    def test_to_dict_more(self):
        """ tests to_dict method """
        my_dict = self.obj.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.obj.created_at, time)

    def test_from_dict_basic(self):
        """tests from_dict method """
        my_dict = self.obj.to_dict()
        obj1 = BaseModel(**my_dict)
        self.assertEqual(obj1.id, self.obj.id)
        self.assertEqual(obj1.updated_at, self.obj.updated_at)
        self.assertEqual(obj1.created_at, self.obj.created_at)
        self.assertEqual(obj1.__class__.__name__,
                         self.obj.__class__.__name__)

    def test_from_dict_kwargs(self):
        """ tests the from_dict method of BaseModel """
        self.obj.student = 'ALX'
        my_dict = self.obj.to_dict()
        self.assertEqual(my_dict['student'], 'ALX')
        obj1 = BaseModel(**my_dict)
        self.assertEqual(obj1.created_at, self.obj.created_at)
        self.assertEqual(obj1.updated_at, self.obj.updated_at)

    def test_unique_id(self):
        """ test uniqueness ofid in BaseModel objects """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(self.obj.id, obj1.id)
        self.assertNotEqual(self.obj.id, obj2.id)

    def test_id_type_string(self):
        """ test id in BaseModel is a string """
        self.assertEqual(type(self.obj.id), str)

    def test_updated_time(self):
        """ test that updated time gets updated """
        time1 = self.obj.updated_at
        self.obj.save()
        time2 = self.obj.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)
