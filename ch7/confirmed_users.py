"""
module name: confirmed_users.py

description:
    pulls users from an unconfirmed list of users, verifies the users, and adds
    them to a list of confirmed users

author: L g
created: 2026-02-05
last modified: 2026-02-05
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

def verify_users(users_to_verify):
    """
    returns a list of vetted users

    args:
        users_to_verify: list of users to check their statut

    returns:
        list of users who passed verification

    raises:
        none
    """
    confirmed_users = []

    while (users_to_verify):
        current_user = users_to_verify.pop()
        print(f"verifying user: {current_user.title()}\n")
        confirmed_users.append(current_user)
    # end while
    
    print("the following users have been confirmed: \n")
    for index, user in enumerate(confirmed_users, start=1):
        print(f"{index}. {user.title()}\n")
    # end for
# end verify_users()

########################
# main app starts here #
########################
unconfirmed_users = [ 'alice', 'bob', 'elon', ]
confirmed_users = verify_users(unconfirmed_users)
