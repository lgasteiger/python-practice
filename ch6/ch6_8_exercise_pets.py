import ch6_fun_library

def create_pet_dict(pet_num, pet_name, owner_name, pet_type="dog", pet_breed="chihuahua", pet_weight=0, pet_age=0):
    """
    this function will return a new dictionary of pet data
    """
    new_pet_dict = {
        "ref_num": pet_num,
        "name": pet_name,
        "owner": owner_name,
        "type": pet_type,
        "breed": pet_breed,
        "weight": pet_weight,
        "age": pet_age,
    }

    return new_pet_dict
# end create_pet_dict

############################
# main program starts here #
############################
print("*****test adding new pets to dictionary*****")
pets_lst = []

pet_luke = create_pet_dict("00001", "luke", "mom", "dog", "chihuahua", 14, 8)
pets_lst.append(pet_luke)
pet_joseph = create_pet_dict("00002", "joseph", "l g", "cat", "leopard spotted", 10, 1)
pets_lst.append(pet_joseph)
pet_future = create_pet_dict("00003", "belgian", "l g")
pets_lst.append(pet_future)
ch6_fun_library.print_list_items(pets_lst)
