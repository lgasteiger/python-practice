"""
module name: ch7_1_rental_car.py

description:
    prompts the user of what type of rental car they would like

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

from ch6.ch6_fun_library import get_valid_input

############################
# main program starts here #
############################
rental_car = get_valid_input(
    "please enter the type of rental car you are interested in: "
) # end get_valid_input()

print(f"please let me see if i can find you a '{rental_car.title()}' method "
      f"of transport. one moment please..."
) # end print()
