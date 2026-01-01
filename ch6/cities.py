import ch6_fun_library

"""
filename: cities.py

author: gasteiger, L g
version: 1.0
"""

def get_city_popln():
    """
    returns the population of the city

    args:
        none

    returns:
        the population of the city
    
    raises:
        none 
    """
    while True:
        popln_num = ch6_fun_library.get_valid_input(
            "please enter the city's current population number without "
            "commas: "
        ) # end get_valid_input()
        
        if ch6_fun_library.is_numeric(popln_num):
            return popln_num
        else:
            print(
                f"!!!!!sorry, the city population must be number. the "
                f"'{popln_num}' value entered is not numeric data!!!!!"
            ) # end print()
            
            if not ch6_fun_library.is_continue():
                return 0
            # end if
        # end if
    # end while
# end get_city_popln()
    
def get_city_info(cities_info):
    """
    retrieves the city information from the user from the keyboard including
    the country of origin, population, and a fun fact

    args:
        cities_info: dictionary data structure containing current city info

    returns:
        none

    raises:
        none
    """
    city_name = ch6_fun_library.get_valid_input("please enter the city name: ")
    city_stats = {}

    country_name = ch6_fun_library.get_valid_input(
        "please enter the city's country of origin: "
    ) # end get_valid_input()
    city_stats["country"] = country_name

    city_popln = int(get_city_popln())
    city_stats["population"] = city_popln

    city_fact = ch6_fun_library.get_valid_input(
        f"please enter a fun fact about the city of {city_name}: "
    ) # end get_valid_input()
    city_stats["fact"] = city_fact

    cities_info[city_name] = city_stats
# end get_city_info(cities_info)

############################
# main program starts here #
############################
common_cities = {
    "sf": {
        "country": "usa",
        "populution": 3000000,
        "fact": "golden gate bridge",
    },
    "la": {
        "country": "usa",
        "population": 10000000,
        "fact": "hollywood",
    },
} # end common_cities dict
ch6_fun_library.print_dict_elem(common_cities)

while True:
    get_city_info(common_cities)
    if not ch6_fun_library.is_continue():
        break
    # end if
# end while
ch6_fun_library.print_dict_elem(common_cities)
