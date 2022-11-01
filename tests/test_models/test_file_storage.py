#!/usr/bin/env python3
""" Test module for the the FileStorage class """


import inspect
import json
import pep8
import unittest

from models.base_model import BaseModel
from models.engine import file_storage
from models import storage
from models.engine.file_storage import FileStorage


class Test_FileStorage_Doc(unittest.TestCase):
    """ Tests class for the FileStorage doc strings"""

    def test_file_storage_pep8_conformance(self):
        """ Tests for pep8style conformance of the base model module """
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style error (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """ Tests for pep8style conformance of the test_file_storage"""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(["tests/test_models/file_storage.py"])
        self.assertEqual(outcome.total_errors, 1,
                         "Found code style error (and warnings).")

    def test_file_storage_docstring(self):
        """ tests if the file_storage module has a documentation """
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_FileStorage_docstring(self):
        """ tests if the FileStorage class docstring is present """
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_FileStorage_methods_docstring(self):
        """ tests if the methods in the class are documented """

        bm = inspect.getmembers(FileStorage, inspect.isfunction)
        for method in bm:
            self.assertTrue(len(method[1].__doc__) >= 1)

class Test_FileStorage(unittest.TestCase):
    """ Tests for the class FileStorage attributes and methods """

    def setUp(self):
        """ sets up an instance and  filestoarge for testing"""
        self.objs = [BaseModel(), BaseModel(), BaseModel()]
        for obj in self.objs:
            storage.new(obj)
        storage.save()

    def tearDown(self):
        """ teardown after each test """
        del self.objs

    def test_type(self):
        """type checks for FileStorage"""
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_save(self):
        """testing the save method of FileStorage """
        self.objs[0].save()
        with open("storage.json", 'r', encoding='utf-8') as f:
            json_dict = json.loads(f.read())
        anchor = "{}.{}".format(self.objs[0].__class__.__name__,
                                str(self.objs[0].id))
        self.assertEqual(json_dict[anchor], self.objs[0].to_dict())

        bad_key = 'BaseModel.112345678909876543'
        try:
            self.assertRaises(json_dict[bad_key], KeyError)
        except:
            pass

    def test_reload(self):
        """tests reload functionality for FileStorage """
        storage.reload()
        obj_dict = storage.all()
        anchor = "{}.{}".format(self.objs[1].__class__.__name__,
                                str(self.objs[1].id))
        self.assertNotEqual(obj_dict[anchor], None)
        self.assertEqual(obj_dict[anchor].id, self.objs[1].id)
        bad_key = 'BaseModel.112345678909876543'
        try:
            self.assertRaises(obj_dict[bad_key], KeyError)
        except:
            pass

    def test_FileStorage_delete_functionality(self):
        """ testing deletion functionality of the storage engine"""
        obj_dict = storage.all()
        anchor = "{}.{}".format(self.objs[2].__class__.__name__,
                                str(self.objs[2].id))
        self.assertEqual(obj_dict[anchor].id, self.objs[2].id)

        del obj_dict[anchor]
        storage.save()
        obj_dict = storage.all()

        try:
            self.assertRaises(obj_dict[anchor], KeyError)
        except:
            pass

    def test_FileStorage_new_with_valid_object(self):
        """ testing new method of FileStorage with a valid instance"""
        obj = BaseModel()
        storage.new(obj)
        obj_dict = storage.all()
        anchor = "{}.{}".format(obj.__class__.__name__, str(obj.id))
        self.assertEqual(obj_dict[anchor] is obj, True)

    def test_FileStorage_new_with_invalid_object(self):
        """ testing new mehtod of FileStorage with invalid object argument """
        try:
            self.assertRaises(storage.new('Francis'), TypeError)
            self.assertRaises(storage.new(None), TypeError)
        except:
            pass
