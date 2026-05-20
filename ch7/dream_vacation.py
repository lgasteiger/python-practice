"""
module name: dream_vacation.py

description:
    prompts for the participant's name and response.
    
author: L g
created: 2026-05-19
last modified: 2026-05-19
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

from ch7.ch7_fun_library import get_polling_data, print_polling_data

############################
# main program starts here #
############################
polling_prompt = "if you could visit one place in the world, " \
"where would you go? "
my_polling_dict = get_polling_data(polling_prompt)
print_polling_data(my_polling_dict)
