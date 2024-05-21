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
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        Resets __objects and __file_path for isolation of test cases.
        """
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__objects = {}
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """
        Tear down method for each test case.
        Cleans up the JSON file.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """
        Test the all() method.
        """
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """
        Test the new() method.
        """
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """
        Test the save() method.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]['id'], obj.id)

    def test_reload(self):
        """
        Test the reload() method.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, obj.id)

    def test_reload_no_file(self):
        """
        Test the reload() method when the JSON file does not exist.
        """
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()

