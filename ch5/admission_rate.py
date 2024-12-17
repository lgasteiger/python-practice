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

def determine_admin_rate():
    """
    this function will determine the admission rate based on the person's age
    group
    """
    try:
        age_input = int(input(f"please enter your age: "))
        persons_admin_rate = f"${get_admin_rate(age_input):.2f}"
        print(
            f"with the person's age of '{age_input}', the person's " +
            f"admission rate is: {persons_admin_rate}"
        ) # end print()
    except TypeError as e:
        print(
            f"!!!!!TypeError() exception raised, {e}!!!!!"
        ) # print()
    except ValueError as e:
        print(
            f"!!!!!ValueError() exception raised, only numeric values are " +
            f"acceptable, {e}!!!!!"
        )
    except Exception as e:
        print(
            f"sorry, but there was an unexpected, unhandled exception " +
            f"raised, {e}"
        ) # end print()
    # end try...except
# end determine_admin_rate()

############################
# main program starts here #
############################
print("**********test person's admissions rate**********")
start_time = time.time()
determine_admin_rate()
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the time it took in seconds for 'determine_admin_rate()' to complete " +
    f"was: {elapsed_time}\n"
) # end print()
