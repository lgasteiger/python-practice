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
from ch8.ch8_fun_library import make_pizza_from_file
from datetime import datetime

########################
# main app starts here #
########################
todays_datetime = datetime.now()
date_only = todays_datetime.strftime("%Y-%m-%d")
time_only = todays_datetime.strftime("%H:%M:%S")

print(
    f"**********Testing make_pizza_v2 with flat file on {date_only} @ "
    f"{time_only}**********"
) # end print()
flat_file_path = Path(".") / "data" / "input_files" / "orders_2026_06_12.csv"
pizza_output_file = make_pizza_from_file(flat_file_path)