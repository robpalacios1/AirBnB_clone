#!/usr/bin/python3
"""Test cases for the User class.x"""
import unittest
import uuid
import os
from datetime import datetime
from datetime import date
from models.base_model import BaseModel
from models.user import User
from models import storage


class UserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if (os.path.exists("storage.json") and
                os.path.isfile("storage.json")):
            os.remove("storage.json")

    def test_instance(self):
        instance = User()
        self.assertIsInstance(instance, User)

    def test_instance_subclass(self):
        instance = User()
        self.assertIsInstance(instance, BaseModel)

    def test_instance_with_args(self):
        instance = User(1)
        self.assertIsInstance(instance, User)

    def test_check_for_instance_member_id(self):
        instance = User()
        self.assertTrue(hasattr(instance, "id"))

    def test_check_for_instance_member_updated_at(self):
        instance = User()
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_check_for_instance_member_created_at(self):
        instance = User()
        self.assertTrue(hasattr(instance, "created_at"))

    def test_instance_from_dict(self):
        instance = User(
            email="john117@protonmail.com",
            password="bsbsbs2019",
            first_name="Master",
            last_name="Chief")
        self.assertIsInstance(instance, User)

    def test_instance_member_email(self):
        instance = User()
        instance.email = "maynard@toolband.com"
        self.assertEqual("maynard@toolband.com", instance.email)

    def test_instance_member_first_name(self):
        instance = User()
        instance.first_name = "Maynard James"
        self.assertEqual("Maynard James", instance.first_name)

    def test_instance_member_last_name(self):
        instance = User()
        instance.last_name = "Keenan"
        self.assertEqual("Keenan", instance.last_name)

    def test_instance_member_password(self):
        instance = User()
        instance.password = "memeReviewByPewDiePie2019"
        self.assertEqual("memeReviewByPewDiePie2019", instance.password)

    def test_instance_is_in_storage(self):
        instance = User()
        self.assertIn(instance, storage.all().values())

    def tearDown(self):
        for attr in storage.__dict__:
            if "__objects" in attr:
                setattr(storage, attr, {})
        if (os.path.exists("storage.json") and os.path.isfile("storage.json")):
            os.remove("storage.json")
