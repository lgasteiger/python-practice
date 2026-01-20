"""
module name: parrot.py

description:
    this app will regurgitate strings entered, using the keyboard, back to the
    screen. the stopping case is when the "quit" string is entered

author: L g
created: 2026-01-19
last modified: 2026-01-19
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
try:
    while True:
        user_str = get_valid_input(
            "please tell me something, and i will repeat it back to you: "
        ) # end get_valid_input()
        if user_str is not None:
            print(f"here is the exact same message: '{user_str}'\n")
        # end if
        
        if not is_continue():
            break
        # end if
    # end while
except TypeError as e:
    print(f"!!!!!a TypeError exception occured, {e}!!!!!")
except ValueError as e:
    print(f"!!!!!a ValueError exception occured, {e}!!!!!")
except Exception as e:
    print(f"!!!!!an unhandled, unexpected exception occured, {e}!!!!!")
# end try...except

