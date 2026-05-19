"""
module name: no_pastrami.py

description:
    prints to the display that no pastrami sandwiches are available at this
    time.
    
author: L g
created: 2026-05-16
last modified: 2026-05-16
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

from ch6.ch6_fun_library import get_valid_input, is_continue, print_dict_elem
from ch7.ch7_fun_library import get_sandwich_orders, process_sandwich_orders

def remove_pastrami_order(original_sandwich_orders):
    """
    this function will remove and key/value pairs with the sandwich value of
    'pastrami'.

    args:
        original_dict: the requested sandwich dict with all the user's 
        sandwich requewsts.

    returns:
        original_dict with no key/value pairs of the 'pastrami' sandwich value

    raises:
        none
    """
    updated_sandwich_orders = {
        name: sandwich for name, sandwich in original_sandwich_orders.items()
        if sandwich != 'pastrami'
    } # end updated_sandwich_orders dict

    return updated_sandwich_orders
# end remove_pastrami_order()

########################
# main app starts here #
########################
print("*****processing sandwich orders*****")
my_sandwich_orders = {
    "gasteiger": "pastrami",
    "negley": "pastrami",
} # end dictionary

print("!!!!!printing hard coded pastriami dict!!!!!")
print_dict_elem(my_sandwich_orders)
print()
user_sandwich_orders = get_sandwich_orders()
merged_sandwich_orders = my_sandwich_orders | user_sandwich_orders
print()
print("*****printing merged sandwich orders*****")
print_dict_elem(merged_sandwich_orders)
print()
modified_sandwich_orders = remove_pastrami_order(merged_sandwich_orders)
process_sandwich_orders(modified_sandwich_orders)
