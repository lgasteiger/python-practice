import time

def is_elem_exists(toppings_list, topping_elem):
    """
    this function will determine if topping_elem arg exists in toppings_list
    """
    if topping_elem in toppings_list:
        return True
    else:
        return False
    # end if
# end is_elem_exists()

def test_elem_exists(popular_toppings, topping_choice):
    try:
        start_time = time.time()
        if (is_elem_exists(popular_toppings, topping_choice)):
            output_mess = (
                f"good news, the '{topping_choice}' element exists in the " +
                f"list"
            ) # end output_mess
            print(output_mess)
        else:
            output_mess = (
                f"sorry, the '{topping_choice}' element does not exist in " +
                f"the list"
            ) # end output_mess
            print(output_mess)
        # end if
        end_time = time.time()
        elapsed_time = end_time - start_time
        print_message = (
            f"the time in seconds it took to complete all processes was " +
            f"{elapsed_time} seconds\n"
        ) # end print_message
        print(print_message)
    except Exception as e:
        print_message = (
            f"!!!!!there was an unexpected, unhandled exception, {e} !!!!!\n"
        ) # end print_message
        print(print_message)
    # end try...catch
# end test_elem_exists(popular_toppings, topping_choice)
        
def is_banned_user(curr_banned_list, banned_user):
    """
    this function test to see if a currently identifed banned user exists in 
    the list of updated list of banned users
    """
    if banned_user not in curr_banned_list:
        output_mess = (
            f"{banned_user.title()}, you can post a response if you wish"
        ) # end output_mess
        print(output_mess)
    else:
        output_mess = (
            f"you can NOT post a response at this time, sorry " +
            f"{banned_user.title()}"
        ) # end output_mess
        print(output_mess)
    # end if
# end is_banned_user(curr_banned_list, banned_user)
        
def test_is_banned_user(pub_banned_list, identified_user):
    """
    this function tests is_banned_user() against the identified test cases
    """
    try:
        start_time = time.time()
        is_banned_user(pub_banned_list, identified_user)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print_message = (
            f"the time in seconds it took to complete all processes was " +
            f"{elapsed_time} seconds\n"
        ) # end print_message
        print(print_message)
    except Exception as e:
        output_mess = (
            f"!!!!!an unexpected, unhandled exception occurred, {e}!!!!!\n"
        ) # end output_mess
        print(output_mess)
    # end try...catch
# end test_is_banned_user(pub_banned_list, identified_user)

###################
# app starts here #
###################

###############
# test case 1 #
###############
print("*****test case 1*****")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
search_topping = "mushrooms"
test_elem_exists(requested_toppings, search_topping)

###############
# test case 2 #
###############
print("*****test case 2*****")
search_topping = "pepperoni"
test_elem_exists(requested_toppings, search_topping)

###############
# test case 3 #
###############
print("*****test case 3*****")
banned_users = ['andrew', 'caroline', 'david']
suspected_user = 'marie'
test_is_banned_user(banned_users, suspected_user)

###############
# test case 4 #
###############
print("*****test case 4*****")
suspected_user = 'caroline'
test_is_banned_user(banned_users, suspected_user)
