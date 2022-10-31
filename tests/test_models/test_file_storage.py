#!/usr/bin/env python3
""" Test module for the the FileStorage class """


import inspect
import pep8
import unittest

from models.engine import file_storage
from models.engine.file_storage import FileStorage


class Test_FileStorage_Doc(unittest.TestCase):
    """ Tests class for the Base Model doc strings"""

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
