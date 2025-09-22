import ch6_fun_library

"""
filename: pizza.py

author: gasteiger, L g
date: 2025-09-21
version: 1.0
"""

def create_pizza(crust_type, toppings_lst):
    """
    this function will return a pizza dictionary with a crust of type crust_type
    and a list of the pizza toppings in a toppings_lst list data structure 
    """
    pizza = {
        "crust": crust_type,
        "toppings_list": list(toppings_lst)
    } # end pizza dictionary

    return pizza
# end create_pizza()

########################
# main app starts here #
########################
print("*****test the creation of a pizza dictionary and printing the dictionary to the screen display*****")
crust_composition = "thick"
my_toppings_lst = ["cheese", "peperoni", "mushrooms"]
my_pizza_dict = create_pizza(crust_composition, my_toppings_lst)
ch6_fun_library.print_dict_elem(my_pizza_dict)
print()
