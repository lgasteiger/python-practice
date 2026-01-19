"""
module name: ch7_3_multiples_10.py

description:
    prompts the user for a number and reports whether the number is a multiple
    of 10

author: L g
created: 2026-01-16
last modified: 2026-01-16
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
from ch6.ch6_fun_library import is_continue

def verify_multiple_10(num_input):
    """
    prints to the screen whether the inputted number is a multiple of 10

    args: 
        num_input: is the actual number entered

    returns:
        none

    raises:
        none
    """
    try:
        if num_input % 10 == 0:
            print(
                f"yes, the '{num_input}' value is a multiple of 10\n"
            ) # end print()
        else:
            print(
                f"no, sorry the '{num_input}' value is not a multiple of "
                f"10\n"
            ) # end print()
        # end if
    except TypeError as e:
        print(f"!!!!!sorry, a TypeError exception occured, {e}!!!!!\n")
    except ValueError as e:
        print(f"!!!!!sorry, a ValueError exception occured, {e}\n!!!!!")
    except Exception as e:
        print(f"!!!!!sorry, an unhandled, unexpected exception occurred, "
              f"{e}!!!!!\n"
        ) # end print()
    # end try...except
# end verify_multiple_10(num_input)

########################
# main app starts here #
########################
while True:
    input_received = get_natural_num_input("please enter a number: ")
    if input_received is not None:
        verify_multiple_10(input_received)
    # emd of
        
    if not is_continue():
        break
    # end if
# end while
