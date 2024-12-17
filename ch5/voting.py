import time

def test_age(person_age):
    """
    this function tests if person_age is over 18 and eligible to vote
    """
    age_to_vote = 18
    try:
        if isNumericInput(person_age):
            if person_age >= age_to_vote:
                print(
                    f"great news, you are old enough to vote"
                ) # end print()
                isRegisteredVote()
            else:
                print(
                    f"sorry, you are not eligile to vote yet. the legal age " +
                    f"to vote in the U.S. is 18"
                ) # print()
            # end if
        # end if
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(
            f"an unexpected, unhandle exception occured, {e}"
        ) # end print()
    # end if
# end test_age()
        
def isNumericInput(ind_age):
    """
    this function validates if the individual'a age 'ind_age' is a numeric
    value, and it will raise a TypeError exception 
    """
    if isinstance(ind_age, int):
        return True
    else:
        raise TypeError(
            f"!!!!!the value '{ind_age}' is not numeric, please try " +
            f"again!!!!!"
        ) # end TypeError() exceptionb
    # end if
# end isNumericInput(ind_age)
        
def isRegisteredVote():
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
            "!!!!!please only respond with a 'y' or 'n' char!!!!!"
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

###############################
# main app driver starts here #
###############################
print("**********test age of person**********")
person_age = 93
start_time = time.time()
test_age(person_age)
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the time it took in seconds to execute 'test_age()' was " +
    f"{elapsed_time} \n"
) # end print()
