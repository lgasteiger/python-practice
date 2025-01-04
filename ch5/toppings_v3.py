def is_input_blank(screen_input):
    """
    this function will find out if the input from the screen prompt is blank.
    if the screen input is blank, then a ValueError() exception will be raised
    """
    if not screen_input.strip():
        raise ValueError(
            "the input entered was blank and invalid. please try again"
        ) # end ValueError() exception
    # end if
# end is_input_blank(screen_input)
    
def is_valid_flag(flag_entry):
    """
    this function will check whether the appropriate "y" or "n" chars were 
    entered on the screen
    """
    if flag_entry != 'y' and flag_entry != 'Y' and \
        flag_entry != 'n' and flag_entry != 'N':
        raise ValueError(
            f"only the 'y' or 'n' response is acceptable"
        ) # end ValueError() exception
    # end if
# end is_valid_flag(flag_entry)

def is_valid_new_topping(topping_input, toppings_list):
    """
    this function verifies if the topping entered is valid. first, is new 
    topping in the present list of acceptable toppings. then, has the 
    topping already been requested for the current pizza order
    """
    acceptable_toppings = [
        'pepperoni', 'sausage', 'extra cheese', 'anchoives', 'pineapple', 
        'ham' 
    ] # end acceptable_toppings

    is_input_blank(topping_input)
    if topping_input not in acceptable_toppings:
        raise ValueError(
            f"the '{topping_input}' is not an acceptable pizza topping. " +
            f"please try again"
        ) # end ValueError() exception
    # end if
        
    if topping_input in toppings_list:
        raise ValueError(
            f"the '{topping_input}' topping was already requested. " +
            f"please try again"
        ) # end ValueError() exception
    # end if

    return True
# end is_valid_new_topping(topping_input, toppings_list)

def print_pizza_toppings(toppings_ordered):
    """
    prints all the requested toppings for the pizza to the display in sorted
    ascending order
    """
    print(f"*****the current list of pizza toppings*****")
    if not toppings_ordered:
        plain_pizza_ans = input("are you sure you want a plain pizza? (y/n) ")
        plain_pizza_ans = plain_pizza_ans.strip()
        is_input_blank(plain_pizza_ans)
        is_valid_flag(plain_pizza_ans)
        if plain_pizza_ans == "n" or plain_pizza_ans == "N":
            raise IndexError("there are no toppings requested yet")
        # end if
    else:
        sorted_toppings = sorted(toppings_ordered)
        for index, topping in enumerate(sorted_toppings):
            print(f"{index + 1}. {topping}")
        # end for...in
    # end if
# end print_pizza_toppings(toppings_ordered)
    
def display_toppings_menu():
    """
    this function will display the app menu for currently available choices
    """
    print("******************************")
    print("*          MAIN MENU         *")
    print("*                            *")
    print("* 1. print current toppings  *")
    print("* 2. add additional toppings *")
    print("* 3. remove existing topping *")
    print("* 4. exit app                *")
    print("******************************")
# end display_toppings_menu()
    
def is_input_numeric(data_input):
    """
    this function verifies if the inputted val was a number
    """
    if not data_input.isdigit():
        raise ValueError(
            f"the '{data_input}' value is not numeric. please try again"
        ) # end ValueError() exception
# end is_input_numeric(data_input)
    
def is_input_in_range(data_entry):
    """
    this function confirms if the value that was entered is an available menu
    selection
    """
    num_data_entry = int(data_entry)
    if num_data_entry < 1 or num_data_entry > 4:
        raise ValueError(
            f"the '{data_entry}' value is not a valid menu option"
        ) # end ValueError() exception
    # end if
# end is_input_in_range(data_entry)
    
def is_valid_choice(input_resp):
    """
    this function will verify that the 'input_resp' is a valid choice
    """
    is_input_blank(input_resp)
    is_input_numeric(input_resp)
    is_input_in_range(input_resp)

    return True
# end is_valid_choice(input_resp)
    
def get_menu_choice():
    """
    this function will prompt for a main menu toppings selection. if the 
    menu choice is valid, the choice will be returned. 
    """
    prompt_resp = input(f"please enter a menu selection: ")
    print()
    prompt_resp = prompt_resp.strip()
    if is_valid_choice(prompt_resp):
        return prompt_resp
    # end if
# end get_menu_choice()

def is_continue_app():
    """
    this function will determine if the app should continue its routine or
    exit the loop structure
    """
    cont_resp = input(f"would you like to still continue? (y/n) ")
    cont_resp = cont_resp.strip()
    is_input_blank(cont_resp)
    is_valid_flag(cont_resp)
    if cont_resp == "y" or cont_resp == "Y":
        return True
    else:
        return False
    # end if
# end is_continue_app()
    
def is_exit_app():
    """
    this function confirms if the app should end
    """
    exit_switch = input(f"do you want to exit the app? (y/n) ")
    exit_switch = exit_switch.strip()
    is_input_blank(exit_switch)
    is_valid_flag(exit_switch)
    if exit_switch == "y" or exit_switch == "Y":
        return True
    else:
        return False
    # end if
# end is_exit_app()
    
def add_toppings(original_toppings):
    """
    this function will add additional toppings to the pizza order 
    """
    new_topping = input("please enter a new pizza topping: ")
    new_topping = new_topping.strip()
    if is_valid_new_topping(new_topping, original_toppings):
        if new_topping == "green peppers":
            print("sorry, we are out of green peppers right now")
        else:
            original_toppings.append(new_topping)
            print(f"adding '{new_topping}' to the pizza request")
        # end if
    # end if
# end add_toppings(original_toppings)

def is_valid_del_topping(rev_topping, existing_toppings):
    """
    this function will confirm if the toppings that has been requested to be 
    removed is a valid topping for this pizza request
    """
    is_input_blank(rev_topping)
    if rev_topping not in existing_toppings:
        raise ValueError(
            f"the '{rev_topping}' topping has not been requested yet and " +
            f"it cannot be removed")
    # end if

    return True
# end is_valid_del_topping(rev_topping)

def remove_toppings(current_toppings):
    """
    this function will remove a topping from the existing pizza request
    """
    del_topping = input(
        "please enter the topping that you would like removed: "
    ) # end del_topping
    del_topping = del_topping.strip()
    if is_valid_del_topping(del_topping, current_toppings):
        current_toppings.remove(del_topping)
        print(
            f"the '{del_topping}' topping has been deleted from the " +
            f"current pizza request"
        ) # end print()
    # end if
# end remove_toppings(current_toppings)

def test_pizza_toppings_requests():
    """
    this function is the driver for testing the requested pizza toppings 
    """
    pizza_toppings_req = []
    while True:
        try:
            display_toppings_menu()
            menu_choice = int(get_menu_choice())
            if menu_choice == 1:
                print_pizza_toppings(pizza_toppings_req)
            # end if
            
            if menu_choice == 2:
                add_toppings(pizza_toppings_req)
            # end if
                
            if menu_choice == 3:
                remove_toppings(pizza_toppings_req)
            # end if
            
            if menu_choice == 4:
                if is_exit_app():
                    break
                # end if
            # end if
            
            if not is_continue_app():
                break
            # end if
        except ValueError as e:
            print(f"!!!!!a ValueError() exception was raised, {e}!!!!!\n")
        except IndexError as e:
            print(f"!!!!!an IndexError() exception was raised, {e}!!!!!\n")
        except Exception as e:
            print(
                f"!!!!!an unexpected, unhandled exception was raised, " +
                f"{e}!!!!!\n"
            ) # end print()
        # end try...except
    # end while
            
    print("thank you for running the app. hope you have a lovely, " +
          "excellent day"
    ) # end print()
# end test_pizza_toppings_requests()

###################
# app starts here #
###################
test_pizza_toppings_requests()
