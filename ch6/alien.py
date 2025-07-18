def get_dic_value(dic_name, dic_key):
    """
    this function returns the alien's points
    """
    return dic_name[dic_key]
# end get_points()

########################
# main app starts here #
########################
alien_0 = {'color': 'green', 'points': 5}

alien_color = get_dic_value(alien_0, "color")
alien_points = get_dic_value(alien_0, "points")
print(f"the alien's color is: {alien_color}")
print(f"the alien's points is: {alien_points}")
