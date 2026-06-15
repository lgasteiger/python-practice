"""
module name: pizza_orders.py

description:
    reads the current pizza orders from an input, makes the pizza, and writes
    the status of each pizza order.

author: L g
created: 2026-06-12
last modified: 2026-06-12
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
from ch8.ch8_fun_library import make_pizza

########################
# main app starts here #
########################
print("**********testing make pizza's app**********")
file_path = Path(".") / "data" / "orders_2026_06_11.txt"
pizza_output_file = make_pizza(file_path)
