import ch6_fun_library

"""
filename: ch6-5_exercise.py

author: gasteiger, L g
date: 2025-09-08
"""

def get_river_names(major_rivers_dict):
    """
    this function only prints the major river names to the screen 
    """
    for river_name in sorted(set(major_rivers_dict.keys())):
        print(f"{river_name.title()}")
    # end for
# end get_river_names()
    
def get_river_countries(major_rivers_dict):
    """
    this function only prints the major rivers countries to the screen
    """
    for river_country in sorted(set(major_rivers_dict.values())):
        print(f"{river_country.title()}")
    # end for
# end get_river_countries()

###########################
# main program begin here #
###########################
major_rivers_dict = {
    "nile": "egypt",
    "mississippi": "mississippi",
    "iguaso": "argentina",
} # end major_rivers_dict

print("*****test the printing of the major rivers dict*****")
ch6_fun_library.print_dict_elem(major_rivers_dict)
print()

print("*****test printing the major river's unique, sorted dictionary keys ")
print("sorted to the screen*****")
get_river_names(major_rivers_dict)
print()

print("*****test printing the major river's unique, sorted dictionary values ")
print("to the screen*****")
get_river_countries(major_rivers_dict)
print()