import time
    
def get_admin_rate(persons_age):
    """
    this function returns the admission rate according to the 'persons_age'
    value, which was submitted previously
    """
    if persons_age < 4:
        return 0
    elif persons_age >= 4 and persons_age < 18:
        return 25
    elif persons_age >= 65:
        return 20
    else:
        return 40
    # end if
# end get_admin_rate(persons_age)
    
def is_continue():
    user_response = input(
        f"would you like to try again? (y/n) "
    ) # end user_response

    # remove leading and trailing spaces
    user_response = user_response.strip()

    if user_response != 'y' and user_response != 'Y' and \
        user_response != 'n' and user_response != 'N':
        raise ValueError(
            f"please only enter a 'y' or 'n' at the prompt"
        ) # end ValueError() exception
    # end if

    if user_response == 'n' or user_response == 'N':
        return False
    else:
        return True
    # end if
# end is_continue()

def determine_admin_rate():
    """
    this function will determine the admission rate based on the person's age
    group
    """
    while True:
        try:
            start_time = time.time()
            age_input = int(input(f"please enter your age: "))
            persons_admin_rate = f"${get_admin_rate(age_input):.2f}"
            print(
                f"with the person's age of '{age_input}', the person's " +
                f"admission rate is: {persons_admin_rate}"
            ) # end print()
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(
                f"the time it took in seconds for 'determine_admin_rate()' " +
                f"to complete was: {elapsed_time}\n"
            ) # end print()

            if not is_continue():
                break
            # end if
        except TypeError as e:
            print(
                f"!!!!!TypeError() exception raised, {e}!!!!!\n"
            ) # end print()

            if not is_continue():
                break
            # end if
        except ValueError as e:
            print(
                f"!!!!!ValueError() exception raised, only numeric values " +
                f"are acceptable, {e}!!!!!\n"
            ) # end print()

            if not is_continue():
                break
            # end if
        except Exception as e:
            print(
                f"sorry, but there was an unexpected, unhandled exception " +
                f"raised, {e}\n"
            ) # end print()

            if not is_continue():
                break
            # end if
        # end try...except
    # end while
# end determine_admin_rate()

############################
# main program starts here #
############################
print("**********test person's admissions rate**********")
determine_admin_rate()
