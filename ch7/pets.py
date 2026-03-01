"""
module name: pets.py

description:
    prompts user for a pet type to be removed from list. if pet type exists, 
    then the value is removed. otherwise, the pet type is ignored
    
author: L g
created: 2026-02-16
last modified: 2026-02-16
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

from ch6.ch6_fun_library import get_valid_input, is_continue, print_list_items

def remove_pet_type(pet_list):
    """
    prompts for a valid pet type value input from the keyboard. if the pet
    type value exists, the value is removed. otherwise, the value is ignored

    args:
        pet_list is the reference pointer to the list data structure containing
        the current pet type list elements

    returns:
        none

    raises:
        none 
    """
    pet_value = get_valid_input(
        "please enter the pet type that needs to be removed: "
    ) # end get_valide_input()

    while pet_value in pet_list:
        pet_list.remove(pet_value)
    # end while
# end remove_pet_type()

########################
# main app starts here #
########################
pets_dict = [ 'dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat', ]
remove_pet_type(pets_dict)
print_list_items(pets_dict)
