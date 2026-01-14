def print_list_items(list_elements):
    """
    prints out the elements in a list with any nested lists or dictionaries
    to the screen

    args:
        list_elements (List): The List data structure containing the elements
        to be printed to the screen

    returns: 
        none

    raises:
        IndexError: if there is an index out of range when looping through the
        List
    """
    try:
        for index, elem in enumerate(list_elements):
            if isinstance(elem, dict):
                print(f"dict_{index}:")
                print_dict_elem(elem)
            else:
                if isinstance(elem, str):
                    print(f"{index}. {elem.title()}")
                else:
                    print(f"{index}. {elem}")
                # end if
            # end if
        # end for
    except IndexError as e:
        print(f"!!!!!!there was an index out of range or invalid list index, {e}!!!!!\n")
    except ValueError as e:
        print(f"!!!!!a ValueError error occurred, {e}!!!!!\n")
    except TypeError as e:
        print(f"!!!!!a TypeError occurred, {e}!!!!!\n")
    except Exception as e:
        print(
            f"!!!!!sorry, but there was an unexpected, unhandled exception raised, {e}!!!!!\n"
        ) # end print()
    # end try...except
# end print_list_items()

"""
prints out the elements of a dictionary with any nested lists or dictionary
to the screen

args:
    dict_elements (Dictionary): The Dictionary data structure that will be 
    printed to the screen

returns:
    none

raises:
    ValueError: If the expected value is not received
    IndexError: If an out of range index is encountered
"""
def print_dict_elem(dict_elements):
    try:
        for key, value in dict_elements.items():
            if isinstance(value, list):
                print(f"\tkey -> {key.title()}: value ->")
                for index, item in enumerate(value):
                    print(f"\t\tlist index [{index}]: {item}")
                # end for
            elif isinstance(value, dict):
                print(f"key -> {key}")
                for key, contents in value.items():
                    if isinstance(contents, str):
                        print(f"\tkey -> {key.title()}: value -> {contents.title()}")
                    elif isinstance(contents, int):
                        print(f"\tkey -> {key.title()}: value -> {contents:,}")
                    else:
                        print(f"\tkey -> {key.title()}: value -> {contents}")
                    # end if
                # end for
            else:
                if isinstance(value, str):
                    print(f"\tkey -> {key.title()}: value -> {value.title()}")
                elif isinstance(value, int):
                    print(f"\tkey -> {key.title()}: value -> {value:,}")
                else:
                    print(f"\tkey -> {key.title()}: value -> {value}")
                # end if
            # end if
        # end for
    except ValueError as e:
        print(f"!!!!!sorry, but a ValueError occurred, {e}!!!!!\n")
    except TypeError as e:
        print(f"!!!!!sorry, but a TypeError occurred, {e}!!!!!\n")
    except Exception as e:
        print(f"!!!!!sorry, an unexpected error occurred, {e}!!!!!\n")
    # end try...except
# end print_dict_elem()

def is_continue():
    """
    prompts the user if they wish to continue. if the input
    response from the user is 'y' or 'Y', then the app will continue.
    otherwise, the app will end

    args:
        none

    returns:
        True if either the 'y' or 'Y' chars are entered in the keyboard
        otherwise, returns False

    raises:
        Exception: if an unexpected error occurs and needs to be caught and 
                   displayed on the screen to the user
    """
    try:
        while True:
            user_response = input(
                 "would you like to continue with the app? (y/n) "
            ) # end input()

            if user_response.strip():
                if user_response == "y" or user_response == "Y":
                    return True
                else:
                    return False
                # end if
            else:
                print(
                    "!!!!!please enter an input. the input cannot be "
                    "blank\n!!!!!"
                ) # end print()
            #end if
        # end while
    except Exception as e:
        print(f"!!!!!an unexpected, unhandled error occurred, {e}!!!!!\n")
    # end try...except
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
            f"sorry, but there was an unexpected, unhandled exception raised, "
            f"{e}\n"
        ) # end print()
    # end try...except
# end get_person_max()

def get_valid_input(prompt):
    """
    get non-empty input from user, rejecting blank or whitespace-only entries

    args:
        prompt: the string question sent to the console display

    returns:
        non-empty input from the keyboard
    
    raises:
        Exception: if an unexpected, unhandled exception occurs and needs to
                   displayed on the screen for the user
    """
    try:
        while True:
            users_input = input(prompt)
            if users_input.strip():
                return users_input.strip()
            else:
                print(
                    "!!!!!sorry, input cannot be empty. please try "
                    "again!!!!!\n"
                ) # end print()
                if not is_continue():
                    break
                # end if
            # end if
        # end while
    except Exception as e:
        print(
            f"!!!!!sorry, and unexpected, unhandled exception occurred, "
            f"{e}!!!!!\n"
        ) # end print()
    # end try...except
# end get_valid_input(prompt)

def is_numeric(keyboard_input):
    """
    checks if user input from the keyboard is a number including negative
    and decimal numbers

    args:
        user_input: keyboard input captured by console

    returns:
        True if user_input is a number. otherwise, False is returned

    """
    try:
        num_test = float(keyboard_input)
        return True
    except ValueError as e:
        return False
    # end try...except
# end is_numeric()