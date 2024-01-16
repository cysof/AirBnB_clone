#!/usr/bin/python3

"""State Module.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel.
    Attributes:
        name (str): the name of the state
    """
    name = ""
