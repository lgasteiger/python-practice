"""
module name: ex_8_5_cities.py

description:
    accepts from the console a city and its country. t-shirt size and text message that should be 
    printed on the t-shirt. it addition, prints a message on the display which 
    summarizes the size and message printed on the t-shirt

author: L g
created: 2026-06-04
last modified: 2026-06-04
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.

"""
from ch6.ch6_fun_library import is_continue
from ch8.ch8_fun_library import ex_8_5_desc_city

########################
# main app starts here #
########################
while True:
    print("**********exercise 8.5, cities**********")
    ex_8_5_desc_city()

    if not is_continue():
        break
    # end if
# end while
