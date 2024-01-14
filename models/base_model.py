#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models
from models import storage


class BaseModel:
    """BaseModel class for creating and managing instances.

    Attributes:
        id (str): A unique identifier for the instance generated using UUID.
        created_at (datetime): The timestamp when the instance was created.
        updated_at (datetime): The timestamp when the instance was last updated.

    Methods:
        __init__(self, *args, **kwargs):
            Initializes a new instance of the BaseModel class.
        __str__(self):
            Returns a string representation of the instance.
        save(self):
            Updates the `updated_at` attribute with the current datetime.
        to_dict(self):
            Converts the instance to a dictionary representation.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Dictionary containing attribute values for recreation.
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self):
        """Converts the instance to a dictionary representation."""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

