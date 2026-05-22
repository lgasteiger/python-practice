"""
module name: ex_8_2_favorite_book.py

description:
    displays a message to the screen depicting one of the users's favorite
    books

author: L g
created: 2026-05-21
last modified: 2026-05-21
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

from ch6.ch6_fun_library import get_valid_input

def get_favorite_book():
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
# end get_favorite_book()
    
def display_fav_book(title):
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
        f"one of the user's favorite books is: '{title}'"
    ) # end print()
# end display_fav_book()

########################
# main app starts here #
########################
fav_book_response = get_favorite_book()
display_fav_book(fav_book_response)
