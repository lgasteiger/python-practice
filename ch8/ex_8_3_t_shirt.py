"""
module name: ex_8_3_t_shirt.py

description:
    accepts from the console a t-shirt size and text message that should be 
    printed on the t-shirt. it addition, prints a message on the display which 
    summarizes the size and message printed on the t-shirt

author: L g
created: 2026-05-28
last modified: 2026-05-28
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.

"""

from ch8.ch8_fun_library import ex_ch8_3_get_shirt_data, ex_ch8_3_write_shirt
from ch8.ch8_fun_library import ex_ch8_3_write_shirt2

########################
# main app starts here #
########################
print("*****prompting for the t-shirt data*****")
t_shirt_data = ex_ch8_3_get_shirt_data()
print()
print(
    "*****displaying the t-shirt attributes (size, message printed on shirt)"
) # end print()
ex_ch8_3_write_shirt(t_shirt_data["size"], t_shirt_data["text"])
print()
print(
    "*****displays to the screen t-shirt default size of 'L' and message to "
    "'i love python. otherwise, displays to the screen what is entered on the "
    "console*****"
) # end print()
ex_ch8_3_write_shirt2()
ex_ch8_3_write_shirt2("m")
