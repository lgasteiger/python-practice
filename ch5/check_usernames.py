def validate_username(username_reply, existing_usernames):
    """
    this function will confirm is the username entered is unique. if the 
    username isn't unique, another username is requested
    """
    if username_reply.lower() in existing_usernames:
        raise ValueError(
            f"the username entered, {username_reply}, must be unique. " +
            f"please try another username that you believe is unique"
        ) # end ValueError() exception
    else:
        print(
            f"success, the '{username_reply}' username is available, and " +
            f"the username was created successfully"
        ) # end print()
        existing_usernames.appended(username_reply)
    # end if
# end validate_username

def test_curr_usernames():
    """
    this function is the driver for testing the currently used website
    usernames. if the username entered isn't unique, then another username 
    is requested
    """
    curr_usernames = [
        'mgjohn', 'mgbarbara', 'mgjake', 'mgmary', 'mgjoseph', 'mglaura'
    ] # end curr_usernames[]

    # prompt for new username
    # validate username reply input
# end test_curr_usernames()

########################
# main app starts here #
########################
