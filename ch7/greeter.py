"""
module name: greeter.py

description:
    prompts user for string and integer input from the keyboard

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

def verify_age(num_input):
    if num_input >= 21:
        print("$$$$$great time in life$$$$$\n")
    else:
        print("^^^^^almost there in life^^^^^\n")
    # end if
# end is_old_enough()

############################
# main program starts here #
############################
print("**********test string input**********")
name_input = get_valid_input("please enter your name: ")
print(f"hello, {name_input.title()}\n")

prompt = "if you share your name, we can personalize the messages you see."
prompt += "\nwhat is your first name: "
name = get_valid_input(prompt)
print(f"hello, {name.title()}!\n")

print("**********test int input**********")
num_input = ch7_fun_library.get_natural_num_input("please enter your age: ")
if num_input is not None:
    print(f"the inputted age is: {num_input}")
    verify_age(num_input)
# end if
