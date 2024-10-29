def print_pizzas(pizza_list):
    """this function prints the pizza items in the pizza_list data structure"""
    for index, pizza in enumerate(pizza_list):
        my_output = f"pizza #{index + 1} = {pizza}"
        print(my_output)
    # end for
        
    print()
# end print_pizzas

my_pizzas = [
    'pepperoni', 'cheese', 'supreme'
]

friend_pizzas = my_pizzas[:]
my_pizzas.append('vegetarian')
friend_pizzas.append('meat-lovers')

print("**********my favorite pizzas are:**********")
print_pizzas(my_pizzas)

print("**********my friend's pizzas are:**********")
print_pizzas(friend_pizzas)
