"""
module name: ch7_2_restaurant_seating.py

description:
    prompts the user for how many people are in their dinner group. if the
    number of people is greater that eight, then the user will have to wait
    a little while longer. otherwise, the table for the dinner group should
    be ready for seating

author: L g
created: 2026-01-13
last modified: 2026-01-13
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

from ch7_fun_library import get_natural_num_input

def handle_grp_size(curr_grp_size):
    """
    prints to the screen the action taken if the current group size is greater
    than 8. if the current group size is less than or equal to 8, another
    type of message is printed to the display

    args:
        curr_grp_size: the validated integer value previously entered and
        successfully accepted by the console

    returns:
        none

    raises:
        ValueError if the curr_grp_size parameter cannot be used in an 
        arthmetic evaluation
    """

    try:
        if curr_grp_size > 8:
            print("i'm sorry, but you may need to wait a little while longer")
        else:
            print("you table is ready")
        # end if
    except TypeError as e:
        print(f"!!!!!sorry a TypeError exception was encountered, {e}!!!!!")
    except ValueError as e:
        print(f"!!!!!sorry a ValueError exception was encountered, {e}!!!!!")
    except Exception as e:
        print(f"!!!!!sorry an unexpected, unhandled exception was encountered,"
              f" {e}"
        ) # end print()
    # end try...catch
# end handle_grp_size(curr_grp_size)

############################
# main program starts here #
############################
dinner_grp_size = get_natural_num_input(
    "please enter the total number of people in your dinner group: "
) # end get_natural_num_input()

handle_grp_size(dinner_grp_size)
