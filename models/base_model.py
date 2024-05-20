#!/usr/bin/python3
"""Module for the BaseModel class"""

import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        
        Attributes:
            id (str): A unique id for each instance.
            created_at (datetime): The current datetime when an instance is created.
            updated_at (datetime): The current datetime when an instance is created and updated every time the object changes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.
        
        Returns:
            str: String representation in the format [<class name>] (<self.id>) <self.__dict__>.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute `updated_at` with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance's `__dict__`.
        
        Returns:
            dict: A dictionary representation of the instance.
                  Includes a key `__class__` with the class name.
                  The `created_at` and `updated_at` attributes are converted to string objects in ISO format.
        """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        return dict_obj

