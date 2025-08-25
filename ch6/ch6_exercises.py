"""
filename: ch6_exercises.py

author: gasteiger, Lg
version: 1.0
"""

def print_person_list(person_list):
    """
    this function will print the contents of the person list with person
    data dictionaries.
    """
    for index, person_data in enumerate(person_list):
        print(f"person_{index}:")
        for key, value in person_data.items():
            print(f"key -> {key}: value -> {value},")
        # end for
        print()
    # end for
# end print_person_data()
        
def add_person_data(person_list, per_first_name, per_last_name, per_age, 
                    per_city):
    """
    this function will add a new person data dic to the person list
    """
    person_data_dic = {
        "first_name": per_first_name,
        "last_name": per_last_name,
        "age": per_age,
        "city": per_city,
    }
    person_list.append(person_data_dic)
# end add_person_data()
    
def get_person_list_idx(person_list, person_full_name):
    """
    this function will return the person list index containing the person 
    key/value pair to be updated
    """
    try:
        for index, person_data in enumerate(person_list):
            for key, value in person_data.items():
                if key == "first_name":
                    first_name = value
                # end if
            
                if key == "last_name":
                    last_name = value
                # end if
            # end for
        
            person_complete_name = f"{last_name}, {first_name}"
            if person_complete_name.lower() == person_full_name.lower():
                return index
            # end if
        # end for
            
        return -1
    except IndexError as e:
        print(
            f"!!!!!!there was an index out of range or invalid list index, " +
            f"{e}!!!!!"
        ) # end print()
    except TypeError as e:
        print(
            f"!!!!!there was an invalid data type encountered, {e}!!!!!!"
        ) # end print()
    except ValueError as e:
        print(
            f"!!!!!there was invaid value encountered, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"sorry, but there was an unexpected, unhandled exception " +
            f"raised, {e}\n"
        ) # end print()
    # end try...except
# end get_person_list_idx()
    
def update_person_data(person_list, new_first_name="", new_last_name="", 
                       new_age=0, new_city=""):
    """
    this function will update the existing key/value data attributes
    """
    full_name = f"{new_last_name}, {new_first_name}"
    person_data_idx = get_person_list_idx(person_list, full_name)
    if person_data_idx >= 0:
        person_data = person_list[person_data_idx]
        if new_first_name != "":
            person_data["first_name"] = new_first_name
        # end if
            
        if new_last_name != "":
            person_data["last_name"] = new_last_name
        # end if
            
        if new_age != 0:
            person_data["age"] = new_age
        # end if
            
        if new_city != "":
            person_data["city"] = new_city
        # end if
    else:
        add_person_data(person_list, new_first_name, new_last_name, new_age, 
                        new_city)
    # end if
# end update_person_data()

###############################
# main program starting point #
###############################
person_data_dic = { "first_name": "", "last_name": "", "age": 0, "city": "", }
person_data_list = [person_data_dic]

print("*****test adding new person data to person list*****")
p2_first_name = "tom"
p2_last_name = "brady"
p2_age = 50
p2_city = "boston"
add_person_data(person_data_list, p2_first_name, p2_last_name, p2_age, p2_city)
print_person_list(person_data_list)
print()

print("*****test updating existing person record data (no match)*****")
p3_first_name = "patrick"
p3_last_name = "mahomes"
p3_age = 30
p3_city = "kansas city"
update_person_data(person_data_list, p3_first_name, p3_last_name, p3_age, 
                   p3_city)
print_person_list(person_data_list)
print()

print("******test updating existing person record data (with match)******")
first_name = "tom"
last_name = "brady"
city = "tampa bay"
update_person_data(person_data_list, first_name, last_name, 0, city)
print_person_list(person_data_list)
