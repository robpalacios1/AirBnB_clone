#!/usr/bin/python3
"""Unittest cases for Place"""

import unittest
from models.city import City
import pep8
import os


class Test_City(unittest.TestCase):
    """"Class City -Unittest """

    def setUp(self):
        """SetUps tests"""
        pass

    def tearDown(self):
        """"Restart tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_base_model(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_pep8_tests_base(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Checks if docstring exists"""
        self.assertTrue(len(City.__doc__) > 1)
        self.assertTrue(len(City.__init__.__doc__) > 1)
        self.assertTrue(len(City.__str__.__doc__) > 1)
        self.assertTrue(len(City.save.__doc__) > 1)
        self.assertTrue(len(City.to_dict.__doc__) > 1)

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = City()
        self.assertIsInstance(obj, City)

    def test_args(self):
        """Arguments to the instance"""
        b = City(8)
        self.assertEqual(type(b).__name__, "City")
        self.assertFalse(hasattr(b, "8"))
