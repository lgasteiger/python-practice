def is_continue():
    """
    this function will prompt the user to continue the app's loop process
    """
    user_response = input(
        f"would you like to continue? (y/n) "
    ) # end user_response

    if user_response != "y" and user_response != "Y" and \
        user_response != "n" and user_response != "N":
        raise ValueError(
            f"only 'y' and 'n' input values are accepted. please try again"
        ) # end ValueError() exception
    # end if

    if user_response == "n" or user_response == "N":
        return False
    else:
        return True
    # end if
# end is_continue()
    
def handle_continue_resp():
    """
    this function deals with the input responses to the continue prompt
    """
    print()
# end handle_continue_resp()

def is_valid_choice(keyb_sel):
    """
    this function confirms that the keyboard input is valid
    """
    if not keyb_sel.strip():
        raise ValueError(
            f"the input value is blank. please try again"
        ) # end ValueError() exception
    # end if
    
    if keyb_sel.isdigit():
        if int(keyb_sel) < 1 or int(keyb_sel) > 4:
            raise ValueError(
                f"the menu choice entered was invalid. please try again"
            ) # end ValueError() exception
        # end if
    else:
        raise ValueError(
            f"the input value is not numeric. please try again"
        ) # end ValueError() exception
    # end if

    return True
# end is_valid_input(keyb_sel)

def print_fav_fruits(fav_fruits_list):
    """
    this function prints out the current fruit elements in the fav_fruits_list 
    """
    print(f"the exist list of favorite fruits:")
    for index, fruit in enumerate(fav_fruits_list):
        print(
            f"{index + 1}. {fruit}"
        ) # end print()
    # end for...in
    print()
# end print_fav_fruits(fav_fruits_list)
    
def prompt_menu_choice(fav_fruits_table):
    """
    this function accepts for a menu selection from the keyboard
    """
    try:
        input_choice = input(f"please enter a menu selection: ")
        if is_valid_choice(input_choice):
            if int(input_choice) == 1:
                print_fav_fruits(fav_fruits_table)
            elif input_choice == 2:
                print()
            elif input_choice == 3:
                print()
            else: # the keyboard input is 4, representing the choice to exit app
                return False
            # end if
    except ValueError as e:
        print(
            f"!!!!!a ValueError() exception was raised, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!an unexpected, unhandled exception occured, {e}!!!!!"
        ) # end print()
    # end try...except

    return True
# end prompt_menu_choice()

def display_fruit_menu():
    """
    this function displays the current menu for favorite fruits
    """
    print("######################################")
    print("#        Favorite Fruit Menu         #")
    print("#                                    #")
    print("# 1. print current favorite fruits   #")
    print("# 2. add new favorite fruit          #")
    print("# 3. remove favorite fruit           #")
    print("# 4. exit                            #")
    print("######################################")
# end display_fruit_menu()

def test_fav_fruits():
    """
    this function is the driver for the test of available fruits
    """
    favorite_fruits = [
        'apples', 'bananas', 'oranges', 'kiwi', 'watermelon', 'grapes'
    ] # end favorite_fruits list
    display_fruit_menu()

    while True:
        try:
            prompt_menu_choice(favorite_fruits)

            try:
                if is_continue():
                    display_fruit_menu()
                else:
                    break
                # end if
            except ValueError as e:
                print(
                    f"!!!!!a ValueError() exception was raised, {e}!!!!!"
                ) # end print()
            except Exception as e:
                print(
                    f"!!!!!an unhandled, unexpected exception was raised, " + 
                    f"{e}!!!!!"
                ) # end print
            # end try...except
        except ValueError as e:
            print(
                f"!!!!!a ValueError() exception was raised, {e}!!!!!"
            ) #end print()

            try:
                if not is_continue:
                    break
                # end if
            except ValueError as e:
                print(
                    f"!!!!!a ValueError() exception was raised, {e}!!!!!"
                ) # end print()
            except Exception as e:
                print(
                    f"!!!!!an unhandled, unexpected exception was raised, " + 
                    f"{e}!!!!!"
                ) # end print
            # end try...except
        except Exception as e:
            print(
                f"!!!!!an unhandled, unexpected exception was raised, {e}!!!!!"
            ) # end print()

            try:
                if not is_continue:
                    break
                # end if
            except ValueError as e:
                print(
                    f"!!!!!a ValueError() exception was raised, {e}!!!!!"
                    ) # end print()
            except Exception as e:
                print(
                    f"!!!!!an unhandled, unexpected exception was raised, " + 
                    f"{e}!!!!!"
                ) # end print
            # end try...except
        # end try...catch
    # end while
# end test_fav_fruit()

############################
# main program starts here #
############################
test_fav_fruits()
