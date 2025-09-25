"""
filename: ch6_fun_library.py

author: gasteiger, Lg
version: 1.0
"""

"""
name: print_list_items(list_elements, is_dict_item=False)
author: gasteiger, Lg
date: 2025-09-01
description: this function will print out all the items presently in the list
             to the screen 
"""
def print_list_items(list_elements):
    try:
        for index, elem in enumerate(list_elements):
            if isinstance(elem, dict):
                for index, dict_elem in enumerate(list_elements):
                    print(f"dict_{index}:")
                    print_dict_elem(dict_elem)
                # end for
            else:
                print(f"{index}. {elem}")
        # end for
    except IndexError as e:
        print(
            f"!!!!!!there was an index out of range or invalid list index, {e}!!!!!"
        ) # end print()
    except TypeError as e:
        print(
            f"!!!!!there was an invalid data type encountered, {e}!!!!!!"
        ) # end print()
    except ValueError as e:
        print(
            f"!!!!!there was invaid value encountered, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"sorry, but there was an unexpected, unhandled exception raised, {e}\n"
        ) # end print()
    # end try...except
    
# end print_list_items()

"""
name: print_dict_item(dict_elements)
author: gasteiger, Lg
date: 2025-09-01
description: this function will print the key/value pairs of the dictionary
             to the screen
"""
def print_dict_elem(dict_elements):
    try:
        for key, value in dict_elements.items():
            if isinstance(value, list):
                print(f"key -> {key}: value ->")
                for index, item in enumerate(value):
                    print(f"\t{index}. {item}")
                # end for
            elif isinstance(value, dict):
                print(f"key -> {key}")
                for key, contents in value.items():
                    print(f"\tkey -> {key}: value -> {contents}")
                # end for
            else:
                print(f"key -> {key}: value -> {value},")
            # end if
        # end for
    except ValueError as e:
        print(f"!!!!!sorry, but a ValueError occurred, {e}!!!!!")
    except Exception as e:
        print(f"!!!!!sorry, an unexpected error occurred, {e}!!!!!")
    # end try...except
# end print_dict_elem()

def is_continue():
    """
    this function prompts the user if they wish to continue. if the input
    response from the user is 'y' or 'Y', then the app will continue.
    otherwise, the app will end
    """
    try:
        while True:
            user_response = input(
                 "would you like to continue with the app? (y/n) "
            ) # end input()

            if user_response == "":
                print(
                    "!!!!!please enter an input. the input cannot be blank!!!!!"
                ) # end print()
            elif user_response == "y" or user_response == "Y":
                return True
            else:
                return False
            # end if
        # end while
    except ValueError as e:
        print(f"!!!!!a ValueError exception has occurred, {e}!!!!!")
    except Exception as e:
        print(f"!!!!!an unexpected, unhandled error occurred, {e}!!!!!")
    # end try...except
    # end while
# end is_continue()
