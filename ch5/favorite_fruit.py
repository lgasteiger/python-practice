def is_valid_choice(keyb_sel):
    """
    this function confirms that the keyboard input is valid
    """
    if not keyb_sel.strip():
        raise ValueError(f"the input value is blank. please try again")
    # end if
    
    if keyb_sel.isdigit():
        if int(keyb_sel) < 1 or int(keyb_sel) > 4:
            raise ValueError(
                f"the menu choice entered was invalid. please try again"
            ) # end ValueError() exception
        # end if
    else:
        raise ValueError(f"the input value is not numeric. please try again")
    # end if

    return True
# end is_valid_input(keyb_sel)

def print_fav_fruits(fav_fruits_list):
    """
    this function prints out the current fruit elements in the fav_fruits_list 
    """
    print(f"the existing list of favorite fruits:")
    for index, fruit in enumerate(fav_fruits_list):
        print(
            f"{index + 1}. {fruit}"
        ) # end print()
    # end for...in
    print()
# end print_fav_fruits(fav_fruits_list)
    
def del_fav_fruit(curr_fav_fruits):
    """
    this function will prompt for a favorite fruit to be removed from the
    current list of favorite fruits
    """
    # todo: prompt for favorite fruit to delete
    # todo: validate that input response is not blank
    # todo: validate that input response does not already exist in the current 
    # todo: favorite fruit list
# end del_fav_fruit(curr_fav_fruits)
    
def add_fav_fruit(curr_fav_fruits):
    """
    this function will prompt for the favorite fruit to add and append this
    fruit to the list of favorite fruits
    """
    # todo: verify that new favorite fruit does not exist in current list 
    
    try:
        new_fav_fruit = input(f"please enter the newest favorite fruit: ")
        if not new_fav_fruit.strip():
            print(
                f"!!!!!the new favorite fruit value cannot be blank. " +
                f"please try again!!!!!\n"
            ) # end print()
        else:
            curr_fav_fruits.append(new_fav_fruit)
            print()
        # end if
    except ValueError as e:
        print(f"")
    except Exception as e:
        print(f"an unexpected, unhandled exception was raised, {e}")
    # end try...except
# end add_fav_fruit()
    
def prompt_menu_choice(fav_fruits_table):
    """
    this function accepts for a menu selection from the keyboard
    """

    input_choice = input(f"please enter a menu selection: ")
    if is_valid_choice(input_choice):
        if int(input_choice) == 1:
            print_fav_fruits(fav_fruits_table)
        elif int(input_choice) == 2:
            add_fav_fruit(fav_fruits_table)
        elif input_choice == 3:
            print()
        else: # the keyboard input is 4, representing the choice to exit app
            print(f"thank you for your time and have an excellent day")
            return False
        # end if
    # end if

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
    
def is_exit():
    """
    this function confirms that the app is to end
    """
    while True:
        acquired_resp = input(f"are you sure you want to exit? (y/n) ").strip()
        if acquired_resp != "y" and acquired_resp != "Y" and \
            acquired_resp != "n" and acquired_resp != "N":
            raise ValueError(
                f"only 'y' and 'n' values are accepted"
                ) # end ValueError() exception
        # end if
        
        if acquired_resp == "y" or acquired_resp == "Y":
            return True
        else:
            return False
        # end if
    # end while
# end is_exit(attained_input)

def test_fav_fruits():
    """
    this function is the driver for the test of available fruits
    """
    favorite_fruits = [
        'apples', 'bananas', 'oranges', 'kiwi', 'watermelon', 'grapes'
    ] # end favorite_fruits list

    while True:
        try:
            display_fruit_menu()
            if not prompt_menu_choice(favorite_fruits):
                if is_exit():
                    break
                else:
                    print()
                # end if
            # end if
        except ValueError as e:
            print(f"!!!!!a ValueError() exception was raised, {e}!!!!!\n")
        except Exception as e:
            print(
                f"!!!!!an unhandled, unexpected exception was raised, " +
                f"{e}!!!!!\n"
            ) # end print()
        # end try...catch
    # end while
# end test_fav_fruit()

############################
# main program starts here #
############################
test_fav_fruits()
