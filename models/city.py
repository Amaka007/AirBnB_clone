#!/usr/bin/env python3
"""
Module for the City class.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Attributes:
        state_id (str): ID of the state the city belongs to.
        name (str): Name of the city.
    """
    state_id = ""
    name = ""

