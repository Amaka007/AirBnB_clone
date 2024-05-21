#!/usr/bin/env python3
"""
Module for testing the City class.
"""

import unittest
from models.city import City
from datetime import datetime
import uuid
import os

class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        Creates a new instance of City.
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up method for each test case.
        Deletes the City instance.
        """
        del self.city

    def test_id_is_unique(self):
        """
        Test that each instance has a unique ID.
        """
        city2 = City()
        self.assertNotEqual(self.city.id, city2.id)

    def test_created_at_initialization(self):
        """
        Test that created_at is initialized correctly.
        """
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at_initialization(self):
        """
        Test that updated_at is initialized correctly.
        """
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test that to_dict method includes the correct keys.
        """
        city_dict = self.city.to_dict()
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)

    def test_to_dict_output(self):
        """
        Test that to_dict method output is correct.
        """
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['created_at'], self.city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], self.city.updated_at.isoformat())
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertEqual(city_dict['name'], self.city.name)

    def test_str_method(self):
        """
        Test the string representation of the City instance.
        """
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_save_method_updates_updated_at(self):
        """
        Test that the save method updates the updated_at attribute.
        """
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_kwargs_initialization(self):
        """
        Test initialization with kwargs.
        """
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertEqual(new_city.id, self.city.id)
        self.assertEqual(new_city.created_at, self.city.created_at)
        self.assertEqual(new_city.updated_at, self.city.updated_at)

    def test_storage_file_exists_after_save(self):
        """
        Test that the storage file exists after saving the instance.
        """
        self.city.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_uuid_format(self):
        """
        Test that the id is in the correct UUID format.
        """
        try:
            uuid.UUID(self.city.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

if __name__ == '__main__':
    unittest.main()

