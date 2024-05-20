#!/usr/bin/env python3
"""Module for the file storage model class to manage the JSON file storage and deserialization."""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    Handles serialization and deserialization of instances to and from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        
        Returns:
            dict: The dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets obj in __objects with key <obj class name>.id.
        
        Args:
            obj (BaseModel): The object to set in __objects.
        """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the JSON file (__file_path) exists.
        If the file doesn’t exist, no exception is raised.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass

