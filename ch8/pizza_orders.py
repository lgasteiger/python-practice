"""
module name: pizza_orders.py

description:
    reads the current pizza orders from an input, makes the pizza, and writes
    the status of each pizza order.

author: L g
created: 2026-06-12
last modified: 2026-06-18
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.

"""
from pathlib import Path
from ch6.ch6_fun_library import get_valid_input as get_keyboard_input
from ch6.ch6_fun_library import print_dict_elem

from ch8.ch8_fun_library import make_pizza_from_file, make_pizza_from_keyboard
from ch8.ch8_fun_library import get_pizza_size, get_toppings

from datetime import datetime

########################
# main app starts here #
########################
todays_datetime = datetime.now()
date_only = todays_datetime.strftime("%Y-%m-%d")
time_only = todays_datetime.strftime("%H:%M:%S")

print(
    f"**********Testing make_pizza_from_file() on {date_only} at {time_only}"
    f"**********"
) # end print()
flat_file_path = Path(".") / "data" / "input_files" / "orders_2026_06_12.csv"
pizza_output_file = make_pizza_from_file(flat_file_path)
print()

print(
    f"**********Testig make_pizza_from_keyboard() on {date_only} at {time_only}"
    f"***********"
) # end print()
last_name = get_keyboard_input("Please enter your last name: ")
first_name = get_keyboard_input("Please enter your first name: ")
pizza_size = get_pizza_size()
toppings_req_lst = get_toppings()
toppings_req_str = "|".join(toppings_req_lst)
todays_datetime_utf_8 = str(date_only) + "T" + str(time_only)
completed_pizza_order = (
    make_pizza_from_keyboard(todays_datetime_utf_8,
                             last_name, first_name, 
                             pizza_size, pizza_toppings=toppings_req_str, 
                             rating="5 stars"
                            ) # end make_pizza_from_keyboard()
) # end completed_pizza_order
print_dict_elem(completed_pizza_order)
