#!/usr/bin/env python3
"""
Module for testing the Review class.
"""

import unittest
from models.review import Review
from datetime import datetime
import uuid
import os

class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up method for each test case.
        Creates a new instance of Review.
        """
        self.review = Review()

    def tearDown(self):
        """
        Clean up method for each test case.
        Deletes the Review instance.
        """
        del self.review

    def test_id_is_unique(self):
        """
        Test that each instance has a unique ID.
        """
        review2 = Review()
        self.assertNotEqual(self.review.id, review2.id)

    def test_created_at_initialization(self):
        """
        Test that created_at is initialized correctly.
        """
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at_initialization(self):
        """
        Test that updated_at is initialized correctly.
        """
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test that to_dict method includes the correct keys.
        """
        review_dict = self.review.to_dict()
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('__class__', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)

    def test_to_dict_output(self):
        """
        Test that to_dict method output is correct.
        """
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertEqual(review_dict['created_at'], self.review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'], self.review.updated_at.isoformat())
        self.assertEqual(review_dict['place_id'], self.review.place_id)
        self.assertEqual(review_dict['user_id'], self.review.user_id)
        self.assertEqual(review_dict['text'], self.review.text)

    def test_str_method(self):
        """
        Test the string representation of the Review instance.
        """
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_save_method_updates_updated_at(self):
        """
        Test that the save method updates the updated_at attribute.
        """
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_kwargs_initialization(self):
        """
        Test initialization with kwargs.
        """
        review_dict = self.review.to_dict()
        new_review = Review(**review_dict)
        self.assertEqual(new_review.id, self.review.id)
        self.assertEqual(new_review.created_at, self.review.created_at)
        self.assertEqual(new_review.updated_at, self.review.updated_at)

    def test_storage_file_exists_after_save(self):
        """
        Test that the storage file exists after saving the instance.
        """
        self.review.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_uuid_format(self):
        """
        Test that the id is in the correct UUID format.
        """
        try:
            uuid.UUID(self.review.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

if __name__ == '__main__':
    unittest.main()

