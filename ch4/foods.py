def print_foods(food_list):
    """this function prints the food elements in the food list"""
    for index, food in enumerate(food_list):
        food_output = f"{index + 1}. {food}"
        print(food_output)
    # end for
# end print_foods

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("my favorite foods are:")
print_foods(my_foods)

print("\nmy friend's favorite are also:")
print_foods(friend_foods)

my_foods.append('cannoli')
print("\nmy updated food list is:")
print_foods(my_foods)

friend_foods.append('ice cream')
print("\nmy friend's updated food list is now:")
print_foods(friend_foods)
