"""
module name: ex_9_1_restaurant.py

description:
    This class represents and models a restaurans, and it will store a 
    restaurant name and cuisine type. Moreover, it will contain methods that 
    describe the restaurant and indicates whether the restaurant is presently
    open for business.

author: LGG
created: 2026-10-06
last modified: 2026-10-29
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module contains examples from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""
class Restaurant:
    """
    This class represents a Restaurant, and it will model common Restaurant
    behavior and functions. It will store a Restaurants name and cuisine type.
    Also, it will give each instance of a Restaurant the ability to describe
    the Restaurant and share the open or close state of the business.
    """
    def __init__(self, restaurant_name, cuisine_type):
        """
        Constructor of class Restaurant that will initialize the resturant
        name and cuisine type attributes.
        """
        self._restaurant_name = restaurant_name
        self._cuisine_type = cuisine_type
    # end __init__()
# end Restaurant class