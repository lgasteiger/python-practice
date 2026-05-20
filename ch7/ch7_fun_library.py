"""
module name: ch7_fun_library.py

description:
    contains reusable functions originally created in the chapter 7 exercises
    of the "Python Crash Course, 3rd Ed." by Prof. Matthes, E.

author: L g
created: 2026-01-11
last modified: 2026-05-18
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module contains examples from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

from ch6.ch6_fun_library import get_valid_input, is_continue

def get_natural_num_input(prompt_mess):
    """
    description:
        this function will prompt the user for a numeric value from the
        keyboard. if the value entered in the keyboard is a natural number,
        then the value is returned. otherwise, a TypeError exception is raised

    args:
       none

    returns:
        natural number

    raise:
        TypeError: if the value from the keyboard is not a number
    """
    while True:
        try:
            num_input = float(get_valid_input(prompt_mess))
            if num_input >= 0:
                return num_input
            else:
                print("!!!!!negative numbers are not permitted!!!!!\n")
                if not is_continue():
                    break
                # end if
            # end if
        except TypeError as e:
            print(
                f"!!!!!sorry, a TypeError exception was encountered. only "
                f"whole numbers are accepted at this time, {e}!!!!!\n"
            ) # end print()
            if not is_continue():
                break
            # end if
        except ValueError as e:
            print(
                f"!!!!!sorry, a ValueError exception was encountered. only "
                f"whole numbers are accepted at this time, {e}!!!!!\n"
            ) # end print()
            if not is_continue():
                break
            # end if
        except Exception as e:
            print(
                f"!!!!!sorry, an unhandled, unexpected exception occured. "
                f"{e}!!!!!\n"
            ) # end print()
            if not is_continue():
                break
            # end if
        # end try...except
    # end while
    
    return None
# end get_natural_num_input()

def get_sandwich_orders():
    """
    this function will prompt for sandwich orders until no more orders are
    requested. then, a dictionary of sandwich orders is returned

    args:
        none

    returns:
        a dictionary of sandwich orders, including the name of the sandwich
        requester as the dictionary key

    raises:
        none
    """
    sandwich_orders_req = {}
    
    while True:
        new_sandwich_requester = get_valid_input(
            "please enter your name: "
        ) # end get_valid_input()
        new_sandwich_order = get_valid_input(
            "please enter a sandwich type for the order: "
        ) # end get_valid_input()
        sandwich_orders_req[new_sandwich_requester] = new_sandwich_order
        
        if not is_continue():
            break
        # end if
    # end while
    
    return sandwich_orders_req
# end get_sandwich_orders()

def process_sandwich_orders(sandwich_orders):
    """
    this function will process a list of sandwich orders and print the status
    of each order. then, the completed sandwich orders will be deleted from 
    sandwich_orders dictionary and moved to a new completed sandwich orders
    dictionary

    args:
        sandwich_orders: contains a dictionary of sandwich orders

    returns:
        none

    raises:
        none
    """
    completed_sandwich_orders = {}
    for name in list(sandwich_orders.keys()):
        sandwich = sandwich_orders.pop(name)
        print(f"the '{sandwich}' sandwich for '{name}' is ready")
        completed_sandwich_orders[name] = sandwich
    # end for    
# end process_sandwich_orders()

def get_polling_data(user_prompt):
    """
    prompts for person's name and response. stores the response in the 
    user_resp_dict

    args:
        user_resp_dict is the dictionary data structure that will store the 
        participant's name and response 
    
    returns:
        none

    raises:
        none
    """

    user_resp_dict = {}
    while True:
        name = get_valid_input("what is your name: ")
        resp = get_valid_input(user_prompt)
        user_resp_dict[name] = resp

        if not is_continue():
            break
        # end if
    # end while
        
    return user_resp_dict
# end get_polling_data()

def print_polling_data(user_resp_dict):
    """
    prints the polling data in the part_resp dictionary data structure

    args:
        part_resp is the dictionary containing the participant's name and
        response

    returns:
        none

    raises:
        none
    """
    print("\n*****polling results*****")
    for name, resp in user_resp_dict.items():
        print(f"{name} would like to climb '{resp}'")
    # end for
# end print_polling_data()
