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

from ch6.ch6_fun_library import get_valid_input

def write_shirt(size, text_message):
    """
    prints to the display a message summarizing the size of the shirt and the
    message printed on it

    args:
        size: the size of the shirt

        text_message: the message that is to be printed on the shirt

    returns:
        none

    raises:
        none
    """
    print(
        f"the size of the shirt is '{size}', and the message to be printed on "
        f"the shirt is: '{text_message}'\n"
    ) # end print()
# end write_shirt()
    
def get_shirt_data():
    """
    prompts for shirt size and t-shirt message and accepts input from the 
    console. then, returns a dictionary with t-shirt size and message to be 
    printed on shirt

    args:
        none

    returns:
        dictionary with t-shirt size and message printed on it

    raises:
        none 
    """
    t_shirt_dict = {}
    shirt_size = get_valid_input("please enter the size of the t-shirt: ")
    t_shirt_dict["size"] = shirt_size

    shirt_message = get_valid_input(
        "please enter the message that will be printed on the shirt: "
    ) # end get_valid_input()
    t_shirt_dict["text"] = shirt_message
    return t_shirt_dict
# end get_shirt_data()
    
########################
# main app starts here #
########################
print("*****prompting for the t-shirt data*****")
t_shirt_data = get_shirt_data()
print()
print(
    "*****displaying the t-shirt attributes (size, message printed on shirt)"
) # end print()
write_shirt(t_shirt_data["size"], t_shirt_data["text"])
