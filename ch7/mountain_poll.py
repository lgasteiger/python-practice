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

from ch6.ch6_fun_library import get_valid_input, is_continue, print_list_items

def get_polling_data(part_resp):
    """
    prompt for person's name and response. store the response in the part_resp
    dict

    args:
        part_resp is the dictionary data structure that will store the 
        participant's name and response 
    
    
    returns:
        none

    raises:
        none
    """
    while True:
        name = get_valid_input("what is your name: ")
        resp = get_valid_input("which mountain would you like to climb today: ")
        part_resp[name] = resp

        if not is_continue():
            break
        # end if
    # end while
# end get_polling_data()
        
def print_polling_data(part_resp):
    """
    prints the polling data in the part_resp dictionary data structure

    args:
        part_resp is the dictionary containing the participant's name and
        response

    returns:
        none

    raises:
        none
    """
    print("\n*****polling results*****")
    for name, resp in part_resp.items():
        print(f"{name} would like to climb {resp}\n")
    # end for
# end print_polling_data()

########################
# main app starts here #
########################
participant_resp = {}
get_polling_data(participant_resp)
print_polling_data(participant_resp)
