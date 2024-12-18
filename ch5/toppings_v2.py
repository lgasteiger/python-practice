import time

def is_requested_anchovies(topping):
    """this function determines if anchovies was requested as a topping"""
    try:
        if topping != 'anchovies':
            print(
                f"since the requested topping, {requested_topping}, was " + 
                f"not ordered, please hold the anchovies\n"
            ) # end print()
        # end if
    except Exception as e:
        print(
            f"!!!!!an unexpected, unhandled error occurred, {e}!!!!!\n"
        ) # end print()
    # end try...except
# end is_requested_anchovies()
        
def is_continue():
    """
    this function prompts for a response to continuing the app
    """
    user_resp = input(
        f"would you like to continue? (y/n)"
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

def is_valid_topping(topping_req):
    """
    this function verifies if the topping entered is valid 
    """
# end is_valid_topping()

def get_toppings():
    """
    this function prompts for additional toppings for the pizza
    """
    requested_toppings = []
    while True:
        topping_entered = input(
            f"please enter your preferred pizza topping: "
        ) # end topping_entered

        # validate topping input

        # add topping to requested_toppings list
        
    # end while
# end get_toppings()

###################
# app starts here #
###################
start_time = time.time()
requested_topping = 'mushrooms'
is_requested_anchovies(requested_topping)
end_time = time.time()
elapsed_time = end_time - start_time        
print(
    f"the time it took for the function to return was {elapsed_time} seconds\n"
) # end print()
