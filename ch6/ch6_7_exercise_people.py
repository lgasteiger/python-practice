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
# ch6_fun_library.print_list_items(people_list)

first_name = "Floyd (Money)"
last_name = "Mayweather"
age = 50
city = "Grand Rapids"
ch6_fun_library.add_person_data(people_list, first_name, last_name, age, city)
ch6_fun_library.print_list_items(people_list)
