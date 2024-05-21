#!/usr/bin/env python3
"""
Unit tests for the FileStorage class.
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    Unit tests for the FileStorage class.
    """

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            obj_dict = json.load(file)
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.assertIn(key, obj_dict)

    def test_reload(self):
        """Test the reload method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_reload_no_file(self):
        """Test reload with no existing file"""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_classes(self):
        """Test the classes method"""
        classes = self.storage.classes()
        self.assertIn("BaseModel", classes)
        self.assertIn("User", classes)
        self.assertIn("State", classes)
        self.assertIn("City", classes)
        self.assertIn("Amenity", classes)
        self.assertIn("Place", classes)
        self.assertIn("Review", classes)

if __name__ == "__main__":
    unittest.main()

