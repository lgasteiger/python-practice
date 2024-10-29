import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from tutorial_utils.tutorial_helpers import test_print_list

print("test range of cubed nums from 1 to 10")
cubed_nums = []
for value in range(1, 11):
    cubed_nums.append(value ** 3)
# end for
# print(cubed_nums)
test_print_list(cubed_nums)
print()

print("test range of squared nums from 1 to 10 using a list comprehension")
squared_nums = [value**2 for value in range(1, 11)]
test_print_list(squared_nums)
