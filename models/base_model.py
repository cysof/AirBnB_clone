#!/usr/bin/python3

import models
import uuid
from datetime import datetime

""" BaseModel Module this is a Parent class for all other classes
that will be created in the project.
"""

class BaseModel:
    """BaseModel class this class will be for creating and managing instances.
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
                'created_at': '2023-11-06T12:34:56.709001',
                'updated_at': '2023-11-06T12:34:56.709001'}
        """

    def __init__(self, *args, **kwargs):

        """Initializes a BaseModel instance.
        Args:
            *args: Unused.
            **kwargs: Dictionary containing attribute values for recreation.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                time_format = "Y-%m-%dT%H:%M:%S.%f"
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, time_format)
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

def __str__(self):
    """
    Returns a string representations of the instance.

    Returns:
        str: A string containing class name, id, and attribute dictionary.
    """
    return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

def save(self):
    """Updates the `updated_at` attribute with the current datetime.
        """
    self.updated_at = datetime.now()

def to_dict(self):
    obj_dict = self.__dict__.copy()
    obj_dict['created_at'] = self.created_at.isoformat()
    obj_dict['__class__'] = self.__class__.__name__
    obj_dict['updated_at'] = self.updated_at.isoformat()
    return obj_dict
