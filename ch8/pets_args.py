"""
module name: pets_args.py

description:
    displays a message to the screen of a pet's name and type of pet

author: L g
created: 2026-05-24
last modified: 2026-05-24
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.

"""

from ch6.ch6_fun_library import get_valid_input

def describe_pet(owner_name, *, pet_name, animal_type, animal_size, 
                 animal_country):
    """
    displays to the screen the name of the owner's pet and animal type

    args:
        owner_name:

        *: forces subsequent args to be passed by keyword

        pet_name: keyword to force name of pet

        animal_type: keyword to force name of animal

        animal_size: keyword to force size of animal

        animal_country: keyword to force animal country of origin

    returns:
        none

    raises:
        none
    """
    print(f"the owner's name is: {owner_name}")
    print(f"the pet's name is: {pet_name}")
    print(f"the pet's animal type is: {animal_type}")
    print(f"the pet's weight size in kilograms is: {animal_size}")
    print(f"the pet's country of origin is: {animal_country}\n")
# end describe_pet()

def get_pet_weight():
    """
    validates input entered in the console is a numeric value. if the value 
    entered is not a number, then the user is prompted to enter again.
    otherwise, the value is accepted

    args:
        none

    returns:
        number repesenting a pet's weight entered in the console

    raises:
        ValueError: exception raised if the value entered in the console is
        non-numeric 
    """
    while True:
        try:
            pet_size = get_valid_input(
                "please enter the pet's weight in kilograms: "
            ) # end get_valid_input()
            number = float(pet_size)
            return number
            # break # exit the loop once a number is entered
        except ValueError as e:
            print(
                f"invalid input. please only enter a number. {e}\n" 
            ) # end print()
        except Exception as e:
            print(
                f"an unhandled, unexpected error occured. {e}\n"
            ) # end print()
        # end try...except
# end get_pet_weight()
    
def get_pet_data():
    """
    returns pet data dictionary containing pet owners name, pet name, pet type,
    pet weight, and pet country of origin

    args:
        none

    returns:
        dictionary of pet owner data including pet owners name, pet name, 
        pet type, pet weight, and pet country of origin

    raises:
        none
    """
    pet_data_dict = {}
    pet_owner_name = get_valid_input("please enter the pet owners name: ")
    pet_data_dict["owner_name"] = pet_owner_name

    pet_name = get_valid_input("please enter the pet's name: ")
    pet_data_dict["pet_name"] = pet_name

    pet_type = get_valid_input("please enter the pet's type classification: ")
    pet_data_dict["pet_type"] = pet_type

    pet_size = get_pet_weight()
    pet_data_dict["pet_size"] = pet_size

    pet_origin = get_valid_input("please enter the pet's country of origin: ")
    pet_data_dict["pet_origin"] = pet_origin

    return pet_data_dict
# end get_pet_data()

########################
# main app starts here #
########################
pet_input_data = get_pet_data()
print()
print("*****the pet data entered is detailed below*****")
describe_pet(
    pet_input_data["owner_name"],
    pet_name=pet_input_data["pet_name"],
    animal_type=pet_input_data["pet_type"], 
    animal_size=pet_input_data["pet_size"],
    animal_country=pet_input_data["pet_origin"]
) # end describe_pet()
