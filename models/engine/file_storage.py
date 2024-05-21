#!/usr/bin/env python3
"""Module for the file storage model class to manage the JSON file storage and deserialization."""

import json
import os

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

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes
    def reload(self):
        """Deserializes the JSON file to __objects (if the file exists)"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                classes = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review
                }
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = classes[class_name]
                    new_obj = cls(**value)
                    self.new(new_obj)
        except FileNotFoundError:
            pass

