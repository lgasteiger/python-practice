import ch6_fun_library

"""
filename: many_aliens.py

author: gasteiger, L g
date: 2025-09-15
version: 1.0
"""

def create_initial_alien(initial_color="green", initial_points=5, initial_speed="slow"):
    """
    this function will create and return an initial alien creature with default 
    attributes
    """
    alien_being = {
        "color": initial_color,
        "points": initial_points,
        "speed": initial_speed,
    } # end alient_being dict

    return alien_being
# end create_initial_alien()

def add_alien_creature(alien_dict, aliens_collection):
    """
    this function will add the alien_dict dictionary to the aliens_collection
    list
    """
    aliens_collection.append(alien_dict)
# add_alien_creature()
    
def test_initial_aliens(aliens):
    """
    this function will create three original alien dictionarys and adds them
    to the aliens list. then, the key/value pairs of each alien dict is
    printed in the aliens list to the screen display 
    """
    alien_0 = create_initial_alien()
    add_alien_creature(alien_0, aliens_list)
    alien_1 = create_initial_alien("yellow", 10, "medium")
    add_alien_creature(alien_1, aliens)
    alien_2 = create_initial_alien("red", 15, "fast")
    add_alien_creature(alien_2, aliens)
    ch6_fun_library.print_list_items(aliens_list, True)
# end test_initial_aliens()

def create_more_aliens(aliens_lst, range_num):
    """
    this function will create alien dicts with random attributes and add them 
    to the aliens_lst upto range_num
    """
    for alien_num in range(range_num):
        new_alien = create_initial_alien()
        add_alien_creature(new_alien, aliens_lst)
    # end for
# end create_more_aliens()
        
def print_aliens_subset(alien_lst, element_count):
    """
    this function will print the first element_count of items in alient_list
    """
    for idx, alien in enumerate(alien_lst[:element_count]):
        print(f"dict_{idx}")
        ch6_fun_library.print_dict_elem(alien)
    # end for
# end print_aliens_subset()

########################
# main app starts here #
########################
aliens_list = []

print("*****test creating and adding a few initial alien dicts to the aliens list and printing to the screen")
test_initial_aliens(aliens_list)
print()

print("*****test creating an additional 30 alien dicts and printing only a subset of 5 of the alien dicts")
create_more_aliens(aliens_list, 30)
print_aliens_subset(aliens_list, 5)
print()
