#!/usr/bin/python3
"""Module for test base_model"""
from .test_class import TestClassDocumentation
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from unittest import TestCase
import uuid


class TestBaseModel(TestCase):
    """Test cases for Base model"""

    def test_code_review(self):
        """Test documentation and pep8"""
        t = TestClassDocumentation(self, BaseModel)
        t.documentation()
        t.pep8(['models/base_model.py',
                'tests/test_models/test_base_model.py'])

    def test_init(self):
        """Test constructor of base model"""
        obj = BaseModel()
        now = datetime.now().replace(microsecond=0)

        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(str(obj), str)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertEqual(obj.created_at.replace(microsecond=0), now)
        self.assertEqual(obj.updated_at.replace(microsecond=0), now)

    def test_string_representation(self):
        """Test the magic method str"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        id_model = my_model.id

        expected = '[BaseModel] ({}) {}'\
                   .format(id_model, my_model.__dict__)
        self.assertEqual(str(my_model), expected)

    def test_constructor_kwargs(self):
        """Test constructor that has kwargs as attributes values"""
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        json_attributes = obj.to_dict()

        obj2 = BaseModel(**json_attributes)

        self.assertIsInstance(obj2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(obj, obj2)

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        sleep(1)

        now = datetime.now().replace(microsecond=0)
        obj.save()

        self.assertEqual(obj.updated_at.replace(microsecond=0),
                         now)

    def test_dictionary(self):
        """Test to_dict method"""
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89

        output = obj.to_dict()

        self.assertIsInstance(output, dict)

        o_id = output['id']
        updated_at = output['updated_at']
        created_at = output['created_at']
        class_name = output['__class__']
        name = output['name']
        my_number = output['my_number']

        self.assertIsInstance(o_id, str)
        self.assertIsInstance(updated_at, str)
        self.assertIsInstance(created_at, str)
        self.assertIsInstance(class_name, str)
        self.assertIsInstance(name, str)
        self.assertIsInstance(my_number, int)
