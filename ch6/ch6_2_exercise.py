import ch6_fun_library

"""
filename: ch6-2_exercises.py

author: gasteiger, Lg
version: 1.0
"""

def get_user_num_info():
    """
    this function returns from the command line a user's name and favorite 
    number
    """
    while True:
        user_input = input("please enter your name and favorite number: ")
        if user_input == "":
            print("!!!!!please enter a value. the input can not be blank!!!!!")
        else:
            sanitized_input = user_input.strip().lower().split()
            break
        # end if
    # end while
    
    return sanitized_input
# end get_user_num_info()

def add_favorite_num(fav_user_nums, user_list):
    """
    this function will add the key/value pair, user_list[0]/user_list[1],
    where user_list[0] is the user's name and user_list[1] is the user's 
    favorite number, to the fav_user_nums dictionary data structure
    """
    users_name = user_list[0]
    users_fav_num = user_list[1]
    # print(f"+++++key - > {users_name}: value -> {users_fav_num}+++++")
    fav_user_nums[users_name] = users_fav_num 
# end add_favorite_num()

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

print("*****test add new user and favorite num*****")
new_user_info = get_user_num_info()
# print(f"this is the newest user info name and fav number: {new_user_info}")
add_favorite_num(favorite_nums, new_user_info)
ch6_fun_library.print_dict_elem(favorite_nums)
