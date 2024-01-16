#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models

""" BaseModel Module that acts as a Parent class for all other classes
to be created.
"""


class BaseModel:
    """BaseModel class for creating and managing instances.
    Attributes:
        id (str): A unique identifier for the instance generated using UUID.
        created_at (datetime): The timestamp when the instance was created.
        updated_at (datetime): The timestamp when instance was last updated.
    Methods:
        __init__(self, *args, **kwargs):
            Initializes a new instance of the BaseModel class.
        __str__(self):
            Returns a string representation of the instance.
        save(self):
            Updates the `updated_at` attribute with the current datetime.
        to_dict(self):
            Converts the instance to a dictionary representation.
    Example:
        >>> my_instance = BaseModel()
        >>> print(my_instance)
        [BaseModel] (unique_id) {'id': 'unique_id',
        'created_at': '2023-11-06T12:34:56.789000',
        'updated_at': '2023-11-06T12:34:56.789000'}
    """

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance.
        Args:
            *args: Unused.
            **kwargs: Dictionary containing attribute values for recreation.
        """
        if kwargs:
            for key, value in kwargs.items():
                time_format = "%Y-%m-%dT%H:%M:%S.%f"
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, time_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance.
        Returns:
            str: A string containing class name, id, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the `updated_at` attribute with the current datetime.
        Saves the object to the storage.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Converts the instance to a dictionary representation.
        Returns:
            dict: A dictionary containing attribute values.
        """
        class_name = self.__class__.__name__
        dict_data = self.__dict__.copy()
        dict_data["__class__"] = class_name
        dict_data["created_at"] = self.created_at.isoformat()
        dict_data["updated_at"] = self.updated_at.isoformat()

        return dict_data
