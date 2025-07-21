def get_dic_value(dic_name, dic_key):
    """
    this function returns the alien's points
    """
    return dic_name[dic_key]
# end get_points()

def add_dic_value(dic_name, dic_key, dic_value):
    """
    This function add a new key: value pair to the dictionary.
    """
    dic_name[dic_key] = dic_value
# end add_dic_value()
    
def update_dic_value(dic_name, dic_key, dic_value):
    """
    This function will update the specified key value.
    """
    dic_name[dic_key] = dic_value
# end update_dic_value()
    
def determine_pos_inc(dic_name):
    """
    This function will determine the increment value that will move the alien.
    """
    if dic_name['speed'] == 'slow':
        return 1
    elif dic_name['speed'] == 'medium':
        return 2
    else:
        return 3
    # end if
# end determine_pos_inc()

def move_alien_position(dic_name):
    """
    Move the alien to the right.
    Determine how far to move the alien based on its current speed.
    """
    x_increment = determine_pos_inc(dic_name)
    dic_name['x_position'] = dic_name['x_position'] + x_increment
# end move_alien_position()

########################
# main app starts here #
########################
alien_0 = {'color': 'green', 'points': 5}

print("*****Test getting dictionary values*****")
alien_color = get_dic_value(alien_0, "color")
alien_points = get_dic_value(alien_0, "points")
print(f"the alien's color is: {alien_color}")
print(f"the alien's points is: {alien_points}")

new_points = get_dic_value(alien_0, "points")
print(f"You just earned {new_points} points!")
print()

print("*****Test add new dictionary values*****")
add_dic_value(alien_0, "x_position", 0)
add_dic_value(alien_0, "y_position", 25)
print(alien_0)
print()

print("*****Test updating a dictionary value*****")
update_dic_value(alien_0, "color", "yellow")
print(alien_0)
print()

print("*****Test moving alien position based on present speed*****")
add_dic_value(alien_0, "speed", "medium")
update_dic_value(alien_0, "speed", "fast")
move_alien_position(alien_0)
print(f"New alien x-axis: {alien_0['x_position']}")

# update_dic_value(alien_0, "speed", "fast")
# move_alien_position(alien_0)
# print(f"New alien x-axis: {alien_0['x_position']}")
