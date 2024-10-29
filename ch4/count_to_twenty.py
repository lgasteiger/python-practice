import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from tutorial_utils.tutorial_helpers import test_print_list

print("print a list of nums from 1 to 20 inclusive using a list cast")
twenty_nums = list(range(1, 21))
test_print_list(twenty_nums)
print()

print("print a list from 1 to 20 inclusive using a regular for loop")
for value in range(1, 21):
    print(value)
# end for
