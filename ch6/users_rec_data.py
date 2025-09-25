import ch6_fun_library

"""
filename: users_rec_data.py

author: gasteiger, L g
date: 2025-09-21
version: 1.0
"""

def add_new_user_data(users_recs_dict):
    """
    this function adds new user record data to the users records data
    dictionary
    """
    aeinstein = {
        "fname": "albert",
        "lname": "einstein",
        "location": "princeton",
    }

    mcurie = {
        "fname": "marie",
        "lname": "curie",
        "location": "paris",
    }

    users_recs_dict["genius"] = aeinstein
    users_recs_dict["world_changer"] = mcurie
# end add_new_user_data()

########################
# main app starts here #
########################
users = {}
add_new_user_data(users)
ch6_fun_library.print_dict_elem(users)
print()
