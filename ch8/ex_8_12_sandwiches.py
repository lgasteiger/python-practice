"""
module name: ex_8_12_sandwiches.py

description:
    Processes sandwich order requests starting from the console prompt and
    saving sandwich order data to an input file. Then, completes the sandwich
    orders and prints the status to the display and writes the status to an
    output file.

author: L g gasteiger
created: 2026-06-27
last modified: 2026-06-27
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""
from ch8.ch8_fun_library import create_sandwiches

############################
# main program starts here #
############################
print("**********test create_sandwiches**********")
create_sandwiches()
