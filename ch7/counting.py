"""
module name: counting.py

description:
    this app counts from 1 to 5 and prints the results to the screen

author: L g
created: 2026-01-18
last modified: 2026-01-18
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

########################
# main app starts here #
########################
curr_num = 0
while curr_num < 5:
    print(f"the current number is: {curr_num + 1}\n")
    curr_num += 1
# end while
