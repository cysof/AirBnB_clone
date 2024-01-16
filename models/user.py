#!/usr/bin/python3

"""User Module
Tht inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel.
    Creates the User profile to use AirBnB
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
