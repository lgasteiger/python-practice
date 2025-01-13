def is_input_blank(screen_input):
    """
    this function will find out if the input from the screen prompt is blank.
    if the screen input is blank, then a ValueError() exception will be raised
    """
    if not screen_input:
        raise ValueError(
            "the input entered was blank and invalid. please try again"
        ) # end ValueError() exception
    # end if
# end is_input_blank(screen_input)
    
def is_username_exists(desired_username, usernames_already_used):
    """
    this function will raised an exception if the desired username is already
    taken and unavailable for use
    """
    if desired_username.lower() in usernames_already_used:
        raise ValueError(
            f"the username entered, {desired_username}, is already in use. " +
            f"please try again to enter a unique username"
        ) # end ValueError() exception
    # end if
# end is_usernamne_exists(desired_usernanme, usernames_already_used)

def validate_username(username_reply, existing_usernames):
    """
    this function will confirm if the username entered is not blank and unique. 
    if the username isn't unique, another username is requested
    """
    is_input_blank(username_reply)
    is_username_exists(username_reply, existing_usernames)
    print(
        f"success, the '{username_reply}' username is available, and " +
        f"the username was created successfully"
    ) # end print()
    existing_usernames.append(username_reply.lower())
# end validate_username
    
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

def is_continue_app():
    """
    this function will determine if the app should continue its routine or
    exit the loop structure
    """
    cont_resp = input(f"would you like to continue with the app? (y/n) ")
    cont_resp = cont_resp.strip()
    is_input_blank(cont_resp)
    is_valid_flag(cont_resp)
    if cont_resp == "y" or cont_resp == "Y":
        return True
    else:
        return False
    # end if
# end is_continue_app()
    
def new_usernames_input(new_username, new_username_list):
    """
    this function will add new usernames inputted into a list of new usernames
    with no dups
    """
    # if new_username is not blank
    if new_username:
        if new_username not in new_username_list:
            new_username_list.append(new_username.lower())
        # end if
    # end if
# end add_new_usernames(new_username, new_username_list)
        
def compare_username_lists(existing_valid_usernames, proposed_new_usernames):
    """
    this function will compare the check for duplicate usernames betw the 
    current list of valid usernames and newly proposed usernames
    """
    print("**********printing username stats**********")
    for index, proposed_username in enumerate(proposed_new_usernames):
        if proposed_username in existing_valid_usernames:
            print(
                f"{index + 1}.-----sorry, the '{proposed_username}' was " +
                f"already taken. only unique usernames are accepted-----"
            ) # end print()
        else:
            print(
                f"{index + 1}.+++++the proposed username, " +
                f"'{proposed_username}' was available and valid+++++"
            ) # end print()
        # end if
    # end for
# end compare_usernames_lists(existing_valid_usernames, proposed_new_usernames)

def display_main_menu():
    """
    this function will print the current main menu options to the screen
    """
    print("****************************************")
    print("* 1. display exising list of usernames *")
    print("* 2. add new username                  *")
    print("* 3. exit                              *")
    print("****************************************")
# end display_main_menu()

def test_curr_usernames():
    """
    this function is the driver for testing the currently used website
    usernames. if the username entered isn't unique, then another username 
    is requested
    """
    curr_usernames = [
        'mgjohn', 'mgbarbara', 'mgjake', 'mgmary', 'mgjoseph', 'mglaura'
    ] # end curr_usernames[]
    curr_usernames_original = curr_usernames[:]
    new_usernames = []

    while True:
        try:
            username_data = input(
                "please enter a username that you'd like to use: "
            ) # end username_data
            username_data = username_data.strip()
            new_usernames_input(username_data, new_usernames)
            validate_username(username_data, curr_usernames)

            if is_continue_app():
                print()
            else:
                break
            # end if
        except ValueError as e:
            print(f"!!!!!a ValueError() exception was raised, {e}!!!!!\n")
        except IndexError as e:
            print(f"!!!!!an IndexError() exception was raised, {e}!!!!!\n")
        except Exception as e:
            print(
                f"!!!!!an unexpected, unhandled exception was raised, "
                f"{e}!!!!!\n"
            ) # end print()
        # end try...except
    # end while
    
    try:
        compare_username_lists(curr_usernames_original, new_usernames)
    except ValueError as e:
        print(f"!!!!!a ValueError() exception was raised, {e}!!!!!")
    except IndexError as e:
        print(
            f"!!!!!an IndexError() exception was raised, {e}!!!!!")
    except Exception as e:
        print(f"!!!!!an unexpected, unhandled exception was raised, {e}!!!!!")
    # end try...except
# end test_curr_usernames()

########################
# main app starts here #
########################
test_curr_usernames()
