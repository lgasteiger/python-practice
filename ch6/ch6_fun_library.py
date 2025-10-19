def print_list_items(list_elements):
    """
    Prints out the elements in a list with any nested lists or dictionaries
    to the screen

    Args:
        list_elements (List): The List data structure containing the elements
        to be printed to the screen.

    Returns: 
        None

    Raises:
        IndexError: If there is an index out of range when looping through the
    """
    try:
        for index, elem in enumerate(list_elements):
            if isinstance(elem, dict):
                print(f"dict_{index}:")
                print_dict_elem(elem)
            else:
                print(f"{index}. {elem}")
        # end for
    except IndexError as e:
        print(f"!!!!!!there was an index out of range or invalid list index, {e}!!!!!\n")
    except Exception as e:
        print(
            f"!!!!!sorry, but there was an unexpected, unhandled exception raised, {e}!!!!!\n"
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
                    print(f"\tkey -> {key.title()}: value -> {contents.title()}")
                # end for
            else:
                print(f"\tkey -> {key.title()}: value -> {value.title()},")
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

def add_person_data(person_list, per_first_name, per_last_name, per_age, per_city):
    """
    this function will add a new person data dic to the person list
    """
    new_person_num = get_person_max(person_list) + 1
    person_data_dic = {
        "person_num": new_person_num,
        "first_name": per_first_name,
        "last_name": per_last_name,
        "age": per_age,
        "city": per_city,
    }
    person_list.append(person_data_dic)
# end add_person_data()

def get_person_max(person_list):
    """
    this function will calculate a new person number max number
    """
    max_num = 0
    try:
        for index, person_attr in enumerate(person_list):
            for key, value in person_attr.items():
                if key == "person_num":
                    if value > max_num:
                        max_num = value
                    # end if
                # end if
            # end for
        # end for
                        
        return max_num
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
# end get_person_max()
