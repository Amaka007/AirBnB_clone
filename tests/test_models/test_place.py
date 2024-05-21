#!/usr/bin/env python3
"""
Module for testing the Place class.
"""

import unittest
from models.place import Place
from datetime import datetime
import uuid
import os

class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        Creates a new instance of Place.
        """
        self.place = Place()

    def tearDown(self):
        """
        Clean up method for each test case.
        Deletes the Place instance.
        """
        del self.place

    def test_id_is_unique(self):
        """
        Test that each instance has a unique ID.
        """
        place2 = Place()
        self.assertNotEqual(self.place.id, place2.id)

    def test_created_at_initialization(self):
        """
        Test that created_at is initialized correctly.
        """
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at_initialization(self):
        """
        Test that updated_at is initialized correctly.
        """
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test that to_dict method includes the correct keys.
        """
        place_dict = self.place.to_dict()
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('__class__', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)

    def test_to_dict_output(self):
        """
        Test that to_dict method output is correct.
        """
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['created_at'], self.place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'], self.place.updated_at.isoformat())
        self.assertEqual(place_dict['city_id'], self.place.city_id)
        self.assertEqual(place_dict['user_id'], self.place.user_id)
        self.assertEqual(place_dict['name'], self.place.name)
        self.assertEqual(place_dict['description'], self.place.description)
        self.assertEqual(place_dict['number_rooms'], self.place.number_rooms)
        self.assertEqual(place_dict['number_bathrooms'], self.place.number_bathrooms)
        self.assertEqual(place_dict['max_guest'], self.place.max_guest)
        self.assertEqual(place_dict['price_by_night'], self.place.price_by_night)
        self.assertEqual(place_dict['latitude'], self.place.latitude)
        self.assertEqual(place_dict['longitude'], self.place.longitude)
        self.assertEqual(place_dict['amenity_ids'], self.place.amenity_ids)

    def test_str_method(self):
        """
        Test the string representation of the Place instance.
        """
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_save_method_updates_updated_at(self):
        """
        Test that the save method updates the updated_at attribute.
        """
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_kwargs_initialization(self):
        """
        Test initialization with kwargs.
        """
        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)
        self.assertEqual(new_place.id, self.place.id)
        self.assertEqual(new_place.created_at, self.place.created_at)
        self.assertEqual(new_place.updated_at, self.place.updated_at)

    def test_storage_file_exists_after_save(self):
        """
        Test that the storage file exists after saving the instance.
        """
        self.place.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_uuid_format(self):
        """
        Test that the id is in the correct UUID format.
        """
        try:
            uuid.UUID(self.place.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

if __name__ == '__main__':
    unittest.main()

