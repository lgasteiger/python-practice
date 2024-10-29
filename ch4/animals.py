import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from tutorial_utils.tutorial_helpers import test_print_list

#######################
# program starts here #
#######################
common_animals = ['hyena', 'coyote', 'dingo', 'wolf']
test_print_list(common_animals, ", would make a great home defender!")
print("any of these wild animals could deter and/or destroy bad guys!!")
