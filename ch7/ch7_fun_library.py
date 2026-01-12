"""
module name: ch7_fun_library.py

description:
    contains reusable functions originally created in the chapter 7 exercises
    of the "Python Crash Course, 3rd Ed." by Prof. Matthes, E.

author: L g
created: 2026-01-11
last modified: 2026-01-11
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

def get_natural_num_input(prompt_mess):
    """
    description:
        this function will prompt the user for a numeric value from the
        keyboard. if the value entered in the keyboard is a natural number,
        then the value is returned. otherwise, a TypeError exception is raised

    args:
       none

    returns:
        natural number

    raise:
        TypeError: if the value from the keyboard is not a number
    """
    while True:
        try:
            num_input = float(get_valid_input(prompt_mess))
            if num_input >= 0:
                return num_input
            else:
                print("!!!!!negative numbers are not permitted!!!!!\n")
                return None
            # end if
        except TypeError as e:
            print(
                f"!!!!!sorry, a TypeError exception was encountered. only "
                f"whole numbers are accepted at this time!!!!! {e}\n"
            ) # end print()
        except ValueError as e:
            print(
                f"!!!!!sorry, a ValueError exception was encountered. only "
                f"whole numbers are accepted at this time!!!!! {e}\n"
            ) # end print()
        except Exception as e:
            print(
                f"!!!!!sorry, an unhandled, unexpected exception occured. "
                f"{e}!!!!!\n"
            ) # end print()
        # end try...except
    # end while
# end get_natural_num_input()
