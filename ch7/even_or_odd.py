"""
module name: even_or_odd.py

description:
    determines whether an input from the keyboard is an even or odd number

author: L g
created: 2026-01-11
last modified: 2026-01-11
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

import ch7_fun_library

############################
# main program starts hear #
############################
test_num = ch7_fun_library.get_natural_num_input(
    "please enter a number, and it will be determined to be an even or "
    "odd number: "
) # end get_natural_num_input()
if test_num is not None:
    if test_num % 2 == 0:
        print(f"the number '{test_num}' is an even number")
    else:
        print(f"the number '{test_num}' is an odd number")
    # end if
# end if
