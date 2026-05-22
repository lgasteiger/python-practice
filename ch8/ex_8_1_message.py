"""
module name: ex_8_1_message.py

description:
    displays a status message to the screen

author: L g
created: 2026-05-20
last modified: 2026-05-20
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

def display_message(user_response):
    """
    displays a status message from the user the screen

    args:
        user_response: input from the keyboard entered by the user

    returns:
        none

    raises:
        none
    """
    print(
        f"in this chapter of Prof. Matthes' book titled, 'Python Crash Course',"
        f" the topics i learned included, '{user_response}'"
    ) # end print()
# end display_message()
    
def get_user_response():
    """
    prompts the user for concepts they may have learned chapter 8 of Prof.
    Matthes' book named, 'Python Crash Course, 3rd Ed.'

    args:
        none

    returns:
        the user response from the keyboard

    raises:
        none
    """
    user_input = get_valid_input(
        "may i ask what you may have learned in the current chapter? "
    ) # end get_valid_input()

    return user_input
# end get_user_response()

########################
# main app starts here #
########################
user_response_keyboard = get_user_response()
display_message(user_response_keyboard)
