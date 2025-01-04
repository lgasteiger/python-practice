def check_admin_login(curr_users_logged):
    """
    this function will check all recorded logins. if the login was 'admin',
    then a specific response will be printed to the display. otherwise, a
    generic greeting willb e printed to the screen
    """
    if not curr_users_logged:
        raise ValueError(
            "since the list is currently empty, please locate today's " +
            "generated user logins list"
        ) # end ValueError() exception
    else:
        for index, user in enumerate(curr_users_logged):
            if user.lower() == "admin":
                print(f"{index}. hello admin, would you like a status report")
            else:
                print(f"{index}. hello {user}, thank you for logging in again")
            # end if
        # end for
    # end if
# end check_admin_login()

def test_hello_logins():
    """
    this function is the driver for the test of all the user logins in the
    sso auth login procedure
    """
    logins_recorded_yest = ['brad', 'kev', 'admin', 'george', 'admin']
    logins_recorded_today = []
    
    try:
        print("**********test yesterday's user login list**********")
        check_admin_login(logins_recorded_yest)
        print()
        print("**********test empty user login list**********")
        check_admin_login(logins_recorded_today)
    except ValueError as e:
        print(f"!!!!!a ValueError() exception was raised, {e}!!!!!")
    except IndexError as e:
        print(f"!!!!!an IndexError() exception was raised, {e}!!!!!")
    except Exception as e:
        print(f"!!!!!an unexpected, unhandled exception was raised, {e}!!!!!")
    # check_admin_login()
# end test_hello_logins()

########################
# main app starts here #
########################
test_hello_logins()
