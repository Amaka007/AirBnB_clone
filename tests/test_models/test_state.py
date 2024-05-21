#!/usr/bin/env python3
"""
Module for testing the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import os

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        """
        self.model = BaseModel()

    def tearDown(self):
        """
        Clean up method for each test case.
        """
        del self.model

    def test_id_is_unique(self):
        """
        Test that each instance has a unique ID.
        """
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_initialization(self):
        """
        Test that created_at is initialized correctly.
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_initialization(self):
        """
        Test that updated_at is initialized correctly.
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test that to_dict method includes the correct keys.
        """
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_output(self):
        """
        Test that to_dict method output is correct.
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_str_method(self):
        """
        Test the string representation of the BaseModel instance.
        """
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save_method_updates_updated_at(self):
        """
        Test that the save method updates the updated_at attribute.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_kwargs_initialization(self):
        """
        Test initialization with kwargs.
        """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)

    def test_storage_file_exists_after_save(self):
        """
        Test that the storage file exists after saving the instance.
        """
        self.model.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_uuid_format(self):
        """
        Test that the id is in the correct UUID format.
        """
        try:
            uuid.UUID(self.model.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")


if __name__ == '__main__':
    unittest.main()

