import time

def is_requested_anchovies(topping):
    """this function determines if anchovies was requested as a topping"""
    if topping != 'anchovies':
        print(
            f"since the requested topping, {topping}, wasn't anchovies, " + 
            f"please hold the anchovies"
        ) # end print()
    # end if
# end is_requested_anchovies(topping)
        
def is_continue():
    """
    this function prompts for a response to continuing the app
    """
    user_resp = input(
        f"would you like to continue (y/n)? "
    ) # end user_resp
    
    # remove leading and trailing whitespace
    user_resp = user_resp.strip()

    if user_resp != 'y' and user_resp != 'Y' and \
        user_resp != 'n' and user_resp != 'N':
        raise ValueError(
            f"only the 'y' and 'n' responses are acceptable"
        ) # end ValueError() exception
    # end if

    if user_resp == 'n' or user_resp == 'N':
        return False
    else:
        return True
    # end if
# end is_continue()

def is_valid_input(topping_input, toppings_list):
    """
    this function verifies if the topping entered is valid 
    """
    if not topping_input.strip():
        raise ValueError(
            f"the input is blank. please try again"
        ) # end ValueError() exception
    # end if

    if topping_input in toppings_list:
        raise ValueError(
            f"the '{topping_input}' topping was already requested. " +
            f"please try again"
        ) # end ValueError() exception
    # end if

    return True
# end is_valid_topping(topping_input, toppings_list)

def print_pizza_toppings(toppings_ordered):
    """
    prints all the requested toppings for the pizza to the display
    """
    print(
        f"*****the complete list of pizza toppings*****"
    ) # end print()
    for index, topping in enumerate(toppings_ordered):
        print(
            f"{index + 1}. {topping}"
        ) # end print()
    # end for...in
# end print_pizza_toppings(toppings_ordered)

def get_toppings():
    """
    this function prompts for additional toppings for the pizza
    """
    requested_toppings = []
    while True:
        try:
            topping_entered = input(
                f"please enter your preferred pizza topping: "
            ) # end topping_entered

            if is_valid_input(topping_entered, requested_toppings):
                requested_toppings.append(topping_entered)
                print(
                    f"adding '{topping_entered} to the pizza"
                ) # end print()
                is_requested_anchovies(topping_entered)
            # end if

            if not is_continue():
                break
            # end if
        except ValueError as e:
            print(
                f"!!!!!ValueError() exception was raised, {e}!!!!!"
            ) # end print()

            if not is_continue():
                break
            # end if
        except IndexError as e:
            print(
                f"!!!!!IndexError() exception was raised, {e}"
            ) # end print()

            if not is_continue():
                break
            # end if
        except Exception as e:
            print(
                f"!!!!!an unexpected, unhandled exception was raised, {e}!!!!!"
            ) # end print()

            if not is_continue():
                break
            # end if
        # end try...except
    # end while
                
    print_pizza_toppings(requested_toppings)
# end get_toppings()

###################
# app starts here #
###################
start_time = time.time()
get_toppings()
end_time = time.time()
elapsed_time = end_time - start_time        
print(
    f"the time it took for the function to return was {elapsed_time} seconds\n"
) # end print()
