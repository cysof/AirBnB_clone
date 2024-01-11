#!/usr/bin/python3

"""
    Filestorage Module:

    this serialize instance into JSON file and further deserialize JSON File to instance

"""
import os
import json
from datetime import datetime
from models.base_model import BaseModel

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

        """
        Deseializes to Json file
            deserializes the JSON file to restore stored objects.
        (only if the JSON file (__file_path) exists.

        """ 

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, mode='r', encoding='utf-8') as Myfile:
                    data = json.load(Myfile)

                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    obj_instance = class_obj(**value)
                    self.__objects[key] = obj_instance

            except (FileNotFoundError, json.JSONDecodeError) as e:
                pass
