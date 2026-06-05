"""
module name: ch8_fun_library.py

description:
    contains reusable functions originally created in the chapter 8 exercises
    of the "Python Crash Course, 3rd Ed." by Prof. Matthes, E.

author: L g
created: 2026-06-02
last modified: 2026-06-02
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module contains examples from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""
from ch6.ch6_fun_library import get_valid_input

def ex_8_2_get_favorite_book():
    """
    prompts the user for one of their favorite books

    args:
        none

    returns:
        one of the user's favorite books

    raises:
        none
    """

    user_fav_book = get_valid_input(
        "please enter one of your favorite books: "
    ) # end get_valid_input()

    return user_fav_book    
# end ex_8_2_get_favorite_book()
    
def ex_8_2_display_fav_book(title):
    """
    prints to the display screen a message concerning one of the user's
    favorite books

    args:
        title: the user's favorite book

    returns:
        none

    raises:
        none 
    """

    print(
        f"one of the user's favorite books is: '{title}'\n"
    ) # end print()
# end ex_8_2_display_fav_book()

def ex_8_3_write_shirt(size, text_message):
    """
    prints to the display a message summarizing the size of the shirt and the
    message printed on it

    args:
        size: the size of the shirt

        text_message: the message that is to be printed on the shirt

    returns:
        none

    raises:
        none
    """
    print(
        f"the size of the shirt is '{size}', and the message to be printed on "
        f"the shirt is: '{text_message}'\n"
    ) # end print()
# end ex_ch8_3_write_shirt()
    
def ex_8_3_write_shirt2(size="L", display_message="i love python"):
    """
    prints to the display a message summarizing the size of the shirt and the
    message printed on it

    args:
        size: the size of the shirt is default 'L'

        text_message: the message that is to be printed on the shirt is
                      default to 'i love python'

    returns:
        none

    raises:
        none
    """
    print(
        f"the size of the shirt is '{size}', and the message to be printed on "
        f"the shirt is: '{display_message}'\n"
    ) # end print()
# end ex_ch8_3_write_shirt2()
    
def ex_8_3_get_shirt_data():
    """
    prompts for shirt size and t-shirt message and accepts input from the 
    console. then, returns a dictionary with t-shirt size and message to be 
    printed on shirt

    args:
        none

    returns:
        dictionary with t-shirt size and message printed on it

    raises:
        none 
    """
    t_shirt_dict = {}
    shirt_size = get_valid_input("please enter the size of the t-shirt: ")
    t_shirt_dict["size"] = shirt_size

    shirt_message = get_valid_input(
        "please enter the message that will be printed on the shirt: "
    ) # end get_valid_input()
    t_shirt_dict["text"] = shirt_message
    return t_shirt_dict
# end ex_ch8_3_get_shirt_data()

def ex_8_5_desc_city():
    """
    prompts for the name of a city and its country. then, the city and its
    country is printed to the display. the default country parameter value is 
    'United States'.

    args:
        none

    returns:
        none

    raises:
        none 
    """
    city_name = get_valid_input("please enter a city: ")
    country_name = get_valid_input("please enter the city's country: ")
    print(
        f"{city_name.title()} is in {country_name.title()}\n"
    ) # end print()
# ex_ch8_5_desc_city()
