import time

def is_requested_anchovies(topping):
    """this function determines if anchovies was requested as a topping"""
    try:
        if topping != 'anchovies':
            output_message = (
                f"since the requested topping, {requested_topping}, was not " +
                f"ordered, please hold the anchovies\n"
        ) # end output_message
        print(output_message)
        return True
    # end if
    except Exception as e:
        output_message = (
            f"!!!!!an error occurred when attempting to update the " +
            f"tuple: {e}!!!!!\n"
        )
        print(output_message)
        return False
    # end try...except
# end is_requested_anchovies()

###################
# app starts here #
###################
start_time = time.time()
requested_topping = 'mushrooms'
func_status = is_requested_anchovies(requested_topping)
end_time = time.time()

if func_status:
    elapsed_time = end_time - start_time
    output_message = (
        f"the processing function returned a successful value of " +
        f"'{func_status}'\n" +
        f"as a result, the time it took to complete the process = " + 
        f"{elapsed_time} seconds\n"
    )
    print(output_message)
else:
    output_message = (
        f"!!!!!the function returned {func_status}, which was an " +
        f"unsuccessful function return value\n"
    )
    print(output_message)
# end if
