import ch6_fun_library

"""
filename: ch6_10_exercises.py

author: gasteiger, L g
version: 1.0
"""

def get_user_nums(user_prompt):
    """
    this function returns from the command line a user's favorite number(s)

    args:
        user_prompt: string that prompts user for favorite number

    returns:
        List of favorite nums entered by user
    """
    favorite_nums = []
    while True:
        user_input = ch6_fun_library.get_valid_input(user_prompt)
        if ch6_fun_library.is_numeric(user_input):
            favorite_nums.append(user_input)
        else:
            print(
                f"!!!!!sorry, the input, {user_input}, is not a valid number"
                "!!!!!"
            ) #end print()
        if not ch6_fun_library.is_continue():
            break            
        # end if
    # end while
    
    return favorite_nums
# end get_user_nums()

############################
# main program starts here #
############################
favorite_nums = {
    "tom": 21,
    "purdy": 27,
    "mahomes": 30,
    "aikmen": 65,
    "madden": 75,
} # end favorite_nums dict

print("*****test print favorite nums dictionary key/value pairs*****")
ch6_fun_library.print_dict_elem(favorite_nums)
print()

print("*****test add new user and favorite num(s)*****")
new_user = ch6_fun_library.get_valid_input("please enter your first name: ")
user_fav_nums = get_user_nums("please enter your favorite number: ")
favorite_nums[new_user] = user_fav_nums
ch6_fun_library.print_dict_elem(favorite_nums)
