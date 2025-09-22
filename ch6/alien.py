"""
filename: alien.py

author: gasteiger, L g
date: 2025-09-01
version: 1.0
"""

def get_dic_value(dic_name, dic_key):
    """
    this function returns the alien's points
    """
    return dic_name[dic_key]
# end get_points()

def print_dic_contents(dic_name):
    """
    prints the key/value pairs of the dictionary, "dic_name"
    """
    for key, value in dic_name.items():
        print(f"key -> {key}: value -> {value}")
    # end for
# end print_dic_contents()

def add_dic_value(dic_name, dic_key, dic_value):
    """
    this function add a new key: value pair to the dictionary
    """
    dic_name[dic_key] = dic_value
# end add_dic_value()
    
def update_dic_value(dic_name, dic_key, dic_value):
    """
    this function will update the specified key value
    """
    dic_name[dic_key] = dic_value
# end update_dic_value()
    
def determine_pos_inc(dic_name):
    """
    this function will determine the increment value that will move the alien
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
    move the alien to the right
    determine how far to move the alien based on its current speed
    """
    x_increment = determine_pos_inc(dic_name)
    dic_name['x_position'] = dic_name['x_position'] + x_increment
# end move_alien_position()
    
def del_alien_value(dic_name, dic_key):
    """
    deletes the key/value pair of the dictionary
    """
    del dic_name[dic_key]
# end del_alien_value()

########################
# main app starts here #
########################
alien_0 = {
    'color': 'green',
    'points': 5,
} # end alien_0 dic

print("*****test getting dictionary values*****")
alien_color = get_dic_value(alien_0, "color")
alien_points = get_dic_value(alien_0, "points")
print(f"the alien's color is: {alien_color}")
print(f"the alien's points is: {alien_points}")

new_points = get_dic_value(alien_0, "points")
print(f"You just earned {new_points} points!")
print()

print("*****test add new dictionary values*****")
add_dic_value(alien_0, "x_position", 0)
add_dic_value(alien_0, "y_position", 25)
print_dic_contents(alien_0)
print()

print("*****test updating a dictionary value*****")
update_dic_value(alien_0, "color", "yellow")
print_dic_contents(alien_0)
print()

print("*****test moving alien position based on present speed*****")
add_dic_value(alien_0, "speed", "medium")
update_dic_value(alien_0, "speed", "fast")
move_alien_position(alien_0)
print(f"New alien x-axis: {alien_0['x_position']}")
print()

print("*****testing deleting alien dic key/value pair*****")
del_alien_value(alien_0, "points")
print_dic_contents(alien_0)
