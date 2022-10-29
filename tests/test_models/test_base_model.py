#!/usr/bin/env python3
""" Test for the the Base class """


import pep8

import unittest
import os


class Test_BaseModel(unittest.TestCase):
    """ Tests class for the Base Model """

    def setUp(self):
        """ sets up the instance obj for testing the BaseModel class """

        self.obj = BaseModel()

    def tearDown(self):
        """ tears down the obj instance after testing """
        self.obj = None

    def test_pep8_style(self):
        """ Tests for pep8style conformance of the base model module """
        style = pep8.StyleGuide(quiet=true)
        outcome = style.check_files("models/base_model.pyi")
        self.asertEqual(outcome.total_errors, 0,
                        "Found code style error (and warnings).")
