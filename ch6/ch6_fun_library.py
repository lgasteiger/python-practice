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
def print_list_items(list_elements, is_dict_item=False):
    try:
        if is_dict_item == False:
            for index, elem in enumerate(list_elements):
                print(f"{index}. {elem}")
            # end for
        else:
            for index, dict_elem in enumerate(list_elements):
                print(f"dict_{index}:")
                print_dict_elem(dict_elem) 
        # end if
    except IndexError as e:
        print(
            f"!!!!!!there was an index out of range or invalid list index, " +
            f"{e}!!!!!"
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
            f"sorry, but there was an unexpected, unhandled exception " +
            f"raised, {e}\n"
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
    for key, value in dict_elements.items():
        print(f"key -> {key}: value -> {value},")
    # end for
# end print_dict_elem()
