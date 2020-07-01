#!/usr/bin/python3
"""Module for test file storage"""
from unittest import TestCase
from models.engine.file_storage import FileStorage
from tests.test_models.test_class import TestClassDocumentation
import os
import sys


class TestFileStorage(TestCase):
    """Test cases for File Storage"""

    def test_code_review(self):
        """Test documentation and pep8"""
        t = TestClassDocumentation(self, FileStorage)
        t.documentation()
        t.pep8(['models/engine/file_storage.py',
                'tests/test_models/test_engine/test_file_storage.py'])

    def test_init(self):
        """Test constructor"""
        f = FileStorage()
        obj, path = f._FileStorage__objects, f._FileStorage__file_path

        self.assertIsInstance(obj, dict)
        self.assertIsInstance(path, str)

    def test_functions(self):
        """Checks if the functions are defined"""
        f = FileStorage()

        self.assertTrue(hasattr(f, 'all'))
        self.assertTrue(hasattr(f, 'new'))
        self.assertTrue(hasattr(f, 'reload'))
        self.assertTrue(hasattr(f, 'save'))

    def test_all(self):
        """Test method all"""
        f = FileStorage()

        self.assertIsInstance(f.all(), dict)

    def test_example(self):
        """Checks the methods reload and save"""
        # Needs to be implemented
        from models import storage
        from models.base_model import BaseModel

        f = FileStorage()
        all_objs = storage.all()
        status = os.path.exists(f._FileStorage__file_path)
        self.assertTrue(status)

        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        print(my_model)
