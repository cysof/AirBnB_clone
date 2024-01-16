#!/usr/bin/python3

"""Amenity Module.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel.
    Defines amenities that users can choose from in places.
    Attribute:
        name <str> : name of the amenity
    """
    name = ""
