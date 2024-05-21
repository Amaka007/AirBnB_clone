#!/usr/bin/env python3
"""
Module for testing the Amenity class.
"""

import unittest
from models.amenity import Amenity
from datetime import datetime
import uuid
import os

class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        Creates a new instance of Amenity.
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up method for each test case.
        Deletes the Amenity instance.
        """
        del self.amenity

    def test_id_is_unique(self):
        """
        Test that each instance has a unique ID.
        """
        amenity2 = Amenity()
        self.assertNotEqual(self.amenity.id, amenity2.id)

    def test_created_at_initialization(self):
        """
        Test that created_at is initialized correctly.
        """
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_initialization(self):
        """
        Test that updated_at is initialized correctly.
        """
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test that to_dict method includes the correct keys.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('name', amenity_dict)

    def test_to_dict_output(self):
        """
        Test that to_dict method output is correct.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'], self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict['name'], self.amenity.name)

    def test_str_method(self):
        """
        Test the string representation of the Amenity instance.
        """
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_save_method_updates_updated_at(self):
        """
        Test that the save method updates the updated_at attribute.
        """
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_kwargs_initialization(self):
        """
        Test initialization with kwargs.
        """
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertEqual(new_amenity.id, self.amenity.id)
        self.assertEqual(new_amenity.created_at, self.amenity.created_at)
        self.assertEqual(new_amenity.updated_at, self.amenity.updated_at)

    def test_storage_file_exists_after_save(self):
        """
        Test that the storage file exists after saving the instance.
        """
        self.amenity.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_uuid_format(self):
        """
        Test that the id is in the correct UUID format.
        """
        try:
            uuid.UUID(self.amenity.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

if __name__ == '__main__':
    unittest.main()

