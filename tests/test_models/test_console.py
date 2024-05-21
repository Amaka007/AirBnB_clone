#!/usr/bin/env python3
"""
Unit tests for the HBNBCommand class.
"""
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Unittests for the BaseModel class."""

    def test_instance_creation(self):
        """Test if a new instance of BaseModel is correctly created."""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_unique_id(self):
        """Test if two instances of BaseModel have unique ids."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_and_updated_at(self):
        """Test if created_at and updated_at are correctly assigned."""
        instance = BaseModel()
        self.assertEqual(instance.created_at, instance.updated_at)

    def test_save_method(self):
        """Test if save() method updates the updated_at attribute."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        sleep(1)
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict() method creates a dictionary with the correct attributes."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(instance_dict["created_at"], instance.created_at.isoformat())
        self.assertEqual(instance_dict["updated_at"], instance.updated_at.isoformat())

    def test_kwargs_instantiation(self):
        """Test if an instance can be created from a dictionary of attributes."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertEqual(new_instance.id, instance.id)
        self.assertEqual(new_instance.created_at, instance.created_at)
        self.assertEqual(new_instance.updated_at, instance.updated_at)

    def test_str_method(self):
        """Test if the string representation of the instance is correct."""
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_str)

    def test_storage_new(self):
        """Test if a new instance is added to storage."""
        initial_count = len(storage.all())
        instance = BaseModel()
        new_count = len(storage.all())
        self.assertEqual(new_count, initial_count + 1)


if __name__ == "__main__":
    unittest.main()

