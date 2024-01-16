#!/usr/bin/python3

"""FileStorage Module that serializes instances to a JSON file
and deserializes JSON file to instances:
"""

import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class FileStorage:
    """FileStorage class for serializing and deserializing instances
    to/from a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): A dictionary to store objects by class name and id.
    Methods:
        all(self): Returns the dictionary of stored objects.
        new(self, obj): Adds an object to the stored objects.
        save(self): Serializes stored objects to the JSON file.
        reload(self): Deserializes the JSON file to restore stored objects.
    """

    __file_path = "file.json"
    __objects = {}
    # list to hold all classes created
    CLASS_MAP = {"BaseModel": BaseModel, "User": User,
                  "State": State, "City": City, "Place": Place,
                  "Amenity": Amenity, "Review": Review}

    def all(self):
        """Returns the dictionary of stored objects.
        Returns:
            dict: A dictionary of objects.
        """
        return self.__objects

    def new(self, obj):
        """Adds an object to the stored objects.
        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes stored objects to the JSON file.
        """
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            json.dump(serialized, my_file)

    def reload(self):
        """Deserializes the JSON file to restore stored objects.
        (only if the JSON file (__file_path) exists.
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, mode='r') as my_file:
                    data = json.load(my_file)
                for key, value in data.items():
                    obj = self.CLASS_MAP[value['__class__']](**value)
                    self.__objects[key] = obj
            except FileNotFoundError:
                pass
