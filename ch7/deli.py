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

from ch6.ch6_fun_library import get_valid_input, is_continue, print_dict_elem
from ch7.ch7_fun_library import get_sandwich_orders, process_sandwich_orders

############################
# main program starts here #
############################
print("*****processing sandwich orders*****")
sandwich_orders_new = get_sandwich_orders()
process_sandwich_orders(sandwich_orders_new)

print("*****testing sandwich_orders_new purge*****")
print_dict_elem(sandwich_orders_new)
