import time

def alien_status(color_event):
    """
    this function will track the status of the alien's events
    """
    if color_event.lower() == "green":
        print(
            f"you have just earned 5 points"
        ) # end print()
    elif color_event.lower() == "yellow":
        print(
            f"you have just earned 10 points"
        ) # end print()
    elif color_event.lower() == "red":
        print(
            f"you have just earned 15 points"
        ) # end print()
    # end if
# end alien_status()
        
def test_alien_color_statuses(color_status):
    """
    this function will be the driver to test the various alien color statuses
    """
    try:
        alien_status(color_status)
    except ValueError as e:
        print(
            f"!!!!!ValueError() exception raised, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!an unexpected, unhandled error occured, {e}!!!!!"
        ) # end print()
    # end try...except
# end test_alien_color_statuses()

##########################
# driver app starts hers #
##########################
print(
    f"*****testing 'green' alien status color*****"
) # end print
start_time = time.time()
test_alien_color_statuses("green")
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the total time it took in seconds to finish the app functions = " +
    f"{elapsed_time}\n"
) # end print()

print(
    f"*****testing 'yellow' alien status color*****"
) # end print
start_time = time.time()
test_alien_color_statuses("yellow")
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the total time it took in seconds to finish the app functions = " +
    f"{elapsed_time}\n"
) # end print()

print(
    f"*****testing 'red' alien status color*****"
) # end print
start_time = time.time()
test_alien_color_statuses("red")
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the total time it took in seconds to finish the app functions = " +
    f"{elapsed_time}\n"
) # end print()
