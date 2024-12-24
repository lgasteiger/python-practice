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
    
def identify_life_stage(person_age):
    """
    this function determines the stage of life based on a person's age 
    """
    if person_age < 2:
        print(
            f"the person is identified as a baby\n"
        ) # end print()
    elif person_age >= 2 and person_age < 4:
        print(
            f"the person is identified as a toddler\n"
        ) # end print()
    elif person_age >= 4 and person_age < 13:
        print(
            f"the person is identified as a kid\n"
        ) # end print()
    elif person_age >= 13 and person_age < 20:
        print(
            f"the person is identified as a teenager\n"
        ) # end print()
    elif person_age >= 20 and person_age < 65:
        print(
            f"the person is identified as an adult\n"
        ) # print()
    else:
        print(
            f"the person is identified as an elder\n"
        ) # print()
    # end if
# end identify_life_stage(person_age)
        
def get_person_age():
    """
    this function prompts for the person's age and validates the data value
    """
    user_input = input(
        f"please enter the person's age: "
    ) # end user_input

    if not user_input.strip():
        raise ValueError(
            f"the value inputted was blank. please try again"
        ) # end ValueError() exception
    # end if

    if user_input.isdigit():
        return int(user_input)
    else:
        raise ValueError(
            f"the value inputted, '{user_input}', is not an age number. " +
            f"please try again"
        ) # end ValueError() exception
# end get_person_age()
    
def test_life_stages():
    """
    this is the driver to test the app's stages of life conditionals
    """
    while True:
        try:
            inputted_val = get_person_age()
            identify_life_stage(inputted_val)
            
            if not is_continue():
                break
            # end if
        except ValueError as e:
            print(
                f"!!!!!ValueError() exception raised, {e}!!!!!"
            ) # end print()

            try:
                if not is_continue():
                    break
                # end if
            except ValueError as e:
                print(
                    f"!!!!!ValueError() exception raised, {e}!!!!!"
                ) # end print()
            except Exception as e:
                print(
                    f"!!!!!an unexpected, unhandled exception was raised, " +
                    f"{e}!!!!!"
                ) # end print()
            # end try...except
        except TypeError as e:
            print(
                f"!!!!!TypeError() exception raised, {e}!!!!!"
            ) # end print()

            try:
                if not is_continue():
                    break
                # end if
            except ValueError as e:
                print(
                    f"!!!!!ValueError() exception raised, {e}!!!!!"
                ) # end print()
            except Exception as e:
                print(
                    f"!!!!!an unexpected, unhandled exception was raised, " +
                    f"{e}!!!!!"
                ) # end print()
            # end try...except
        except Exception as e:
            print(
                f"!!!!!an unexpected, unhandled exception was raised, {e}!!!!!"
            ) # end print()
            
            try:
                if not is_continue():
                    break
                # end if
            except ValueError as e:
                print(
                    f"!!!!!ValueError() exception raised, {e}!!!!!"
                ) # end print()
            except Exception as e:
                print(
                    f"!!!!!an unexpected, unhandled exception was raised, " +
                    f"{e}!!!!!"
                ) # end print()
            # end try...except
        # end try...except
    # end while
# end test_life_stages()

############################
# main program starts here #
############################
test_life_stages()
