import ch6_fun_library

def add_people_dicts(persons_list):
    """
    this function will add new people data, from a dictionary data structure
    to the "persons_list" data structure
    """
    person_data_dict = {
        "person_num": 0,
        "first_name": "Terrance (Bud)",
        "last_name": "Crawford",
        "age": 38,
        "city": "Omaha",
        "state": "Nebraska"
    } # end person_data_dict dictionary
    
    persons_list.append(person_data_dict)
# end add_people_dicts()

def test_is_continue():
    """
    test the is_continue() function in the ch6_fun_library.py Python file
    """
    while ch6_fun_library.is_continue():
        print("+++++we'll continue to continue+++++")
    # end if
        
    print("-----we're done here-----")
# end test_is_continue()

def prompt_for_new_people():
    """
    this function will prompt the user for new people data from the keyboard
    """
    fullname_input = input("please enter the first name and last name of the new person:")
    fullname_list = fullname_input.strip().lower().split()
    # TODO: validate fullname_list contains only two string elements

    age_input = input("please enter the age of the new person:")
    sanitized_age = age_input.strip()
    # TODO: validate age_input is only of type int

    city_input = input("please enter the city of the new person:")
    sanitized_city = city_input.strip()
# end prompt_for_new_people()
    
def validate_fullname(complete_name):
    """
    this function will validate the fullname entered by the user with their keyboard
    """
# end validate_fullname

########################
# main app starts here #
########################
print("*****test adding and printing a list of dictionaries*****")
people_list = []
first_name = "Terrance (Bud)"
last_name = "Crawford"
age = 38
city = "Omaha"
state = "Nebraska"
ch6_fun_library.add_person_data(people_list, first_name, last_name, age, city)
ch6_fun_library.print_list_items(people_list)

# print("*****test is_continue() function*****")
#test_is_continue()
