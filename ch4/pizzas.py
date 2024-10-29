import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from tutorial_utils.tutorial_helpers import test_print_list

#######################
# program starts here #
#######################
favorite_pizzas = ['cheese', 'meat lovers', 'vegetarian']
test_print_list(favorite_pizzas, " is one of the great pizzas!")
end_message = "i really love pizza!!"
print(end_message)
