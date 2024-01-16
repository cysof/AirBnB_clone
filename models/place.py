#!/usr/bin/python3

"""Place Module
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel.
    Which will contain information on the place User might be interested in.
    Attributes:
        name (str): the name of the Place
        description (str): information about the place
        number_rooms (int): the number of room in the place
        number_bathrooms (int): the number of bathrooms in the place
        max_guest (int): the maximum number of the guests at the same time
        price_by_night (int): the price for a one night in the place
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
        city_id (str): the City id from our City class
        user_id (str): the User id from our User Class
        amenity_ids (list of str): list of Amenity ids
    """
    city_id = ""  # It will be the City.id
    user_id = ""  # It will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # It will be the list of Amenity.id later
