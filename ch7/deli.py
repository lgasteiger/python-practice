"""
module name: deli.py

description:
    provides the state of each sandwich and prints the result to the screen
    display.
    
author: L g
created: 2026-04-30
last modified: 2026-05-01
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

def process_sandwich_orders(sandwich_orders):
    """
    this function will process a list of sandwich orders and print the status
    of each order. then, the completed sandwich orders will be deleted from 
    sandwich_orders dictionary and moved to a new completed sandwich orders
    dictionary

    args:
        sandwich_orders: contains a dictionary of sandwich orders

    returns:
        none

    raises:
        none
    """
    completed_sandwich_orders = {}
    for name in list(sandwich_orders.keys()):
        sandwich = sandwich_orders.pop(name)
        print(f"the '{sandwich}' sandwich for '{name}' is ready")
        completed_sandwich_orders[name] = sandwich
    # end for    
# end process_sandwich_orders()

def get_sandwich_orders():
    """
    this function will prompt for sandwich orders until no more orders are
    requested. then, a dictionary of sandwich orders is returned

    args:
        none

    returns:
        a dictionary of sandwich orders, including the name of the sandwich
        requester as the dictionary key

    raises:
        none
    """
    sandwich_orders_req = {}
    
    while True:
        new_sandwich_requester = get_valid_input(
            "please enter your name: "
        ) # end get_valid_input()
        new_sandwich_order = get_valid_input(
            "please enter a sandwich type for the order: "
        ) # end get_valid_input()
        sandwich_orders_req[new_sandwich_requester] = new_sandwich_order
        
        if not is_continue():
            break
        # end if
    # end while
    
    print()
    return sandwich_orders_req
# end get_sandwich_orders()

############################
# main program starts here #
############################
print("*****processing sandwich orders*****")
sandwich_orders_list = get_sandwich_orders()
process_sandwich_orders(sandwich_orders_list)
