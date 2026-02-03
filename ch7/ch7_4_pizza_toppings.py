"""
module name: ch7_4_pizza_toppings.py

description:
    prompts the user to enter a series of pizza toppings until the user does
    not want to continue

author: L g
created: 2026-02-02
last modified: 2026-02-02
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

from ch6.ch6_fun_library import get_valid_input, is_continue

def process_toppings():
    """
    this function will accept pizza toppings from the user from the keyboard 
    until the user chooses not to continue. a confirmation is printed to the 
    display for every valid pizza topping entered by the user

    args:
        none

    returns:
        none

    raises:
        none
    """
    while True:
        user_topping = get_valid_input("please enter a pizza topping: ")
        print(
            f"to confirm, we'll be adding the '{user_topping}' topping to your " 
            f"pizza order\n"
        ) # end print()

        if not is_continue():
            break
        # end if
    # end while
# end process_toppings()

########################
# main app starts here #
########################
process_toppings()
