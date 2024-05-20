#!/usr/bin/env python3
"""
Unittests for BaseModel class.
"""

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Sets up the test environment before each test.
        """
        self.model = BaseModel()

    def tearDown(self):
        """
        Cleans up the test environment after each test.
        """
        del self.model

    def test_instance_creation(self):
        """
        Test the creation of a BaseModel instance.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_id(self):
        """
        Test that each BaseModel instance has a unique ID.
        """
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_save_method(self):
        """
        Test the save method updates `updated_at` attribute.
        """
        old_updated_at = self.model.updated_at
        sleep(1)
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_str_method(self):
        """
        Test the __str__ method returns the correct string representation.
        """
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(expected_str, str(self.model))

    def test_to_dict_method(self):
        """
        Test the to_dict method returns a dictionary with correct values.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())
        self.assertIn("__class__", model_dict)
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)

if __name__ == "__main__":
    unittest.main()

