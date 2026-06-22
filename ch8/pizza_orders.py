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
from ch8.ch8_fun_library import make_pizza, make_pizza_v2

########################
# main app starts here #
########################
# print("**********testing make pizza's app with text file**********")
# text_file = Path(".") / "data" / "orders_2026_06_11.txt"
# pizza_output_file = make_pizza(text_file)
print()
print("**********testing make pizza's app with flat file**********")
flat_file_path = Path(".") / "data" / "orders_2026_06_12.csv"
pizza_output_file = make_pizza_v2(flat_file_path)
print()
