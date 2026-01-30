"""
module name: cities.py

description:
    this app will regurgitate strings entered, using the keyboard, back to the
    screen. the stopping case is when the "quit" string is entered

author: L g
created: 2026-01-25
last modified: 2026-01-25
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

########################
# main app starts here #
########################
while True:
    city_input = get_valid_input("please enter the city you have visited: ")
    print(f"i would love to go to {city_input.title()}\n")
    if not is_continue():
        break
    # end if
# end while
