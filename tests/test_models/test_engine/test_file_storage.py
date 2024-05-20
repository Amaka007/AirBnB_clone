#!/usr/bin/env python3
"""
Unittests for the FileStorage class.
"""

import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Sets up the test environment before each test.
        Creates a new instance of FileStorage and a BaseModel instance.
        """
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def tearDown(self):
        """
        Cleans up the test environment after each test.
        Deletes the JSON file if it exists and resets the storage.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """
        Test the all method returns the __objects dictionary.
        """
        self.assertEqual(self.storage.all(), {f"BaseModel.{self.model.id}": self.model})

    def test_new(self):
        """
        Test the new method sets an object in __objects.
        """
        model2 = BaseModel()
        self.storage.new(model2)
        self.assertIn(f"BaseModel.{model2.id}", self.storage.all())

    def test_save(self):
        """
        Test the save method serializes __objects to the JSON file.
        """
        self.storage.save()
        with open("file.json", "r") as file:
            obj_dict = json.load(file)
        self.assertIn(f"BaseModel.{self.model.id}", obj_dict)

    def test_reload(self):
        """
        Test the reload method deserializes the JSON file to __objects.
        """
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())
        self.assertIsInstance(self.storage.all()[f"BaseModel.{self.model.id}"], BaseModel)

    def test_reload_no_file(self):
        """
        Test the reload method when the JSON file does not exist.
        Ensures no exception is raised.
        """
        try:
            self.storage.reload()
        except Exception as e:
            self.fail(f"reload raised {type(e).__name__} unexpectedly!")

if __name__ == "__main__":
    unittest.main()

