import time

def is_continue():
    """
    this function prompts the user to continue or exit the app logic
    """
    user_response = input(
        f"do you want to continue the app prompt (y/n)? "
    ) # end user_response

    # remove leading and trailing spaces
    user_response = user_response.strip()

    if user_response != 'y' and user_response != 'Y' and \
        user_response != 'n' and user_response != 'N':
        raise ValueError(
            f"please only enter a 'y' or 'no' for your response"
        ) # end ValueError() exception
    # end if
    
    if user_response == 'n' or user_response == 'N':
        return False
    else:
        return True
    # end if
# end is_continue()

def is_registered_vote():
    """
    this function will determine if the user has registered to vote prior to 
    any upcoming elections
    """
    user_input = input(
        f"in addition, have you registered to vote (y/n)? "
    ) # end input()
    
    if user_input != "y" and user_input != "Y" and \
        user_input != "n" and user_input != "N":
        raise ValueError(
            "please only respond with a 'y' or 'n' char"
        ) #end ValueError() exception
    # end if

    if user_input == "y" or user_input == "Y":
        print(
            f"thank you for registering to vote prior to the next election"
        ) # end print()
    else: # user_input == 'n' or 'N'
        print(
            f"please register to vote before the deadline"
        ) # end print()
    # end if
# end isRegisterVote()

def test_age():
    """
    this function tests if person_age is over 18 and eligible to vote
    """
    age_to_vote = 18
    while True:
        try:
            start_time = time.time()
            persons_age = int(input(f"please enter the age: "))
            if persons_age >= age_to_vote:
                print(
                    f"great news, you are old enough to vote"
                ) # end print()
                is_registered_vote()
            else:
                print(
                    f"sorry, you are not eligile to vote yet. the legal age " +
                    f"to vote in the U.S. is 18"
                    ) # end print()
            # end if
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(
                f"the time it took in seconds to execute 'test_age()' was " +
                f"{elapsed_time} \n"
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
                f"!!!!!ValueError() exception raised, {e}!!!!!\n"
            ) # end print()

            if not is_continue():
                break
            # end if
        except Exception as e:
            print(
                f"!!!!!an unexpected, unhandle exception occured, {e}!!!!!\n"
            ) # end print()

            if not is_continue():
                break
            # end if
        # end try...except
    # end while
# end test_age()

###############################
# main app driver starts here #
###############################
print("**********test age of person**********")
test_age()
