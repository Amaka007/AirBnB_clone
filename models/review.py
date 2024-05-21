#!/usr/bin/env python3
"""
Module for the Review class.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    Attributes:
        place_id (str): ID of the place being reviewed.
        user_id (str): ID of the user writing the review.
        text (str): Text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""

