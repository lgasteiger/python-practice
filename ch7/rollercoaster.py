"""
module name: rollercoaster.py

description:
    determines whether a person is tall enough to ride a roller coaster

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

from ch6.ch6_fun_library import get_valid_input
import ch7_fun_library

############################
# main program starts here #
############################
height = ch7_fun_library.get_natural_num_input("how tall are you in inches? ")
if height is not None:
    if height >= 48:
        print(
            f"yes, with a current height of '{height}', you are tall enough "
            f"to ride\n"
        ) # end print()
    else:
        print(
            f"no sorry, with a current height of '{height}' you will have to "
            f"wait to ride until you are a little older\n"
        ) # end print()
    # end if
# end if
