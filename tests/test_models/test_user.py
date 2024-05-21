#!/usr/bin/env python3
"""
Module for testing the User class.
"""

import unittest
from models.user import User
from datetime import datetime
import uuid
import os

class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        Creates a new instance of User.
        """
        self.user = User()

    def tearDown(self):
        """
        Clean up method for each test case.
        Deletes the User instance.
        """
        del self.user

    def test_id_is_unique(self):
        """
        Test that each instance has a unique ID.
        """
        user2 = User()
        self.assertNotEqual(self.user.id, user2.id)

    def test_created_at_initialization(self):
        """
        Test that created_at is initialized correctly.
        """
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at_initialization(self):
        """
        Test that updated_at is initialized correctly.
        """
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test that to_dict method includes the correct keys.
        """
        user_dict = self.user.to_dict()
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)

    def test_to_dict_output(self):
        """
        Test that to_dict method output is correct.
        """
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'], self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], self.user.updated_at.isoformat())
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)

    def test_str_method(self):
        """
        Test the string representation of the User instance.
        """
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_save_method_updates_updated_at(self):
        """
        Test that the save method updates the updated_at attribute.
        """
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_kwargs_initialization(self):
        """
        Test initialization with kwargs.
        """
        user_dict = self.user.to_dict()
        new_user = User(**user_dict)
        self.assertEqual(new_user.id, self.user.id)
        self.assertEqual(new_user.created_at, self.user.created_at)
        self.assertEqual(new_user.updated_at, self.user.updated_at)

    def test_storage_file_exists_after_save(self):
        """
        Test that the storage file exists after saving the instance.
        """
        self.user.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_uuid_format(self):
        """
        Test that the id is in the correct UUID format.
        """
        try:
            uuid.UUID(self.user.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")


if __name__ == '__main__':
    unittest.main()

