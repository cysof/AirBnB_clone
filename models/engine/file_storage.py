#!/usr/bin/python3

"""
    Filestorage Module:

    this serialize instance into JSON file and further deserialize JSON File to instance

"""



import models
import json
from datetime import datetime
from models.base_model import BaseModel
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

    CLASS_MAP = {"BaseModel": BaseModel,}



    def all(self):
        """
            Dictionary of stored object

            this method returns dictionary of stored objects

            Return: the dictionary returns __objects
        """
        return self.__objects

    def new(self, obj):
        """Adds an object to the stored objects.
            Args:
                obj: The object to be added.
            """
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes stored objects to the JSON file.

        """
        serialized = {}

        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as Myfile:
            json.dump(serialized, Myfile)

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
            except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
                pass
