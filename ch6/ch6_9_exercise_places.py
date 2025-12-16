import ch6_fun_library

############################
# main program starts here #
############################
favorite_places_dict = {
    "san franciso, ca": "john",
    "princeton, nj": "frank",
    "washington, dc": "allison",
}

ch6_fun_library.print_dict_elem(favorite_places_dict)

print("*****testing adding new users and favorite places*****")
try:
    users_name = ch6_fun_library.get_valid_input("please enter your name: ")
    users_place = ch6_fun_library.get_valid_input("please enter a favorite place: ")
    favorite_places_dict[users_place] = users_name
    ch6_fun_library.print_dict_elem(favorite_places_dict)
except IndexError as e:
    print(f"!!!!!an IndexError exception occurred, {e}!!!!!\n")
except Exception as e:
    print(
        f"!!!!!sorry, but an unexpected, unhandled exception occurred, "
        f"{e}!!!!!\n"
    ) # end print()
# end try...except
