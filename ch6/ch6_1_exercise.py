import ch6_fun_library

"""
filename: ch6_1_exercises.py

author: gasteiger, Lg
version: 1.0
"""
    
def get_person_list_idx(person_list, fname, lname, per_num=-1):
    """
    this function will return the person list index containing the person 
    key/value pair(s) to be updated
    """
    try:
        for index, person_data in enumerate(person_list):
            if per_num >= 0:
                for key, value in person_data.items():
                    if key == "person_num":
                        if value == per_num:
                            return index
                        # end if
                    # end if
                # end for
            else:
                full_name = f"{lname}, {fname}"
                for key, value in person_data.items():
                    if key == "first_name":
                        first_name = value
                    # end if
                
                    if key == "last_name":
                        last_name = value
                    # end if
                # end for
                    
                legal_name = f"{last_name}, {first_name}"
                if legal_name == full_name:
                    return index
            # end if
        # end for
        
        return -1
    except IndexError as e:
        print(
            f"!!!!!!there was an index out of range or invalid list index, {e}!!!!!"
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
            f"sorry, but there was an unexpected, unhandled exception raised, {e}\n"
        ) # end print()
    # end try...except
# end get_person_list_idx()
    
def update_person_data(person_list, new_first_name="", new_last_name="", new_age=0, new_city="", person_id=-1):
    """
    this function updates the existing person data dictionary key/value pairs 
    """
    person_data_idx = get_person_list_idx(person_list, new_first_name, new_last_name, person_id)
    
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
        ch6_fun_library.add_person_data(person_list, new_first_name, new_last_name, new_age, new_city)
    # end if
# end update_person_data()
        
def delete_person_data_rec(person_list, del_first_name, del_last_name, person_id=-1):
    """
    this function will delete a person data dictionary record in the person
    list, if it exists
    """
    person_data_idx = get_person_list_idx(person_list, del_first_name, del_last_name, person_id)
    if person_data_idx >= 0:
        person_list.pop(person_data_idx)
    else:
        print("!!!!!no record to delete, person data record does not ")
        print("exist!!!!!")
# end delete_person_data_rec()

###############################
# main program starting point #
###############################
person_data_dic = {
    "person_num": 0, 
    "first_name": "", 
    "last_name": "", 
    "age": 0, 
    "city": "",
} # end person_data_dic 
person_data_list = [person_data_dic]

print("*****test adding new person data to person list*****")
p2_first_name = "tom"
p2_last_name = "brady"
p2_age = 50
p2_city = "boston"
ch6_fun_library.add_person_data(person_data_list, p2_first_name, p2_last_name, p2_age, p2_city)
ch6_fun_library.print_list_items(person_data_list)
print()

print("*****test updating existing person record data (no match)*****")
p3_first_name = "patrick"
p3_last_name = "mahomes"
p3_age = 30
p3_city = "kansas city"
update_person_data(person_data_list, p3_first_name, p3_last_name, p3_age, p3_city)
ch6_fun_library.print_list_items(person_data_list)
print()

print("******test updating existing person record data by person_id ")
print("(with match)******")
person_num = 1
first_name = "tom"
last_name = "brady"
age = 0
city = "tampa bay"
update_person_data(person_data_list, first_name, last_name, age, city, person_num)
ch6_fun_library.print_list_items(person_data_list)
print()

print("*****test updating existing person record data by person full name*****")
first_name = "tom"
last_name = "brady"
city = ""
age = 55
update_person_data(person_data_list, first_name, last_name, age, city)
ch6_fun_library.print_list_items(person_data_list)
print()

print("*****test deleting person list person data dict element with match*****")
first_name = ""
last_name = ""
per_num = 0
delete_person_data_rec(person_data_list, first_name, last_name, per_num)
ch6_fun_library.print_list_items(person_data_list)
print()
