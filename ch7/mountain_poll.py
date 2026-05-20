"""
module name: mountain_poll.py

description:
    prompts for the participant's name and response.
    
author: L g
created: 2026-03-14
last modified: 2026-03-14
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

########################
# main app starts here #
########################
participant_prompt = "which mountain would you like to climb today: "
participant_resp = get_polling_data(participant_prompt)
print_polling_data(participant_resp)
