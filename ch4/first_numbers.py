import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from tutorial_utils.tutorial_helpers import test_print_list

print("test range print from 1 to 5")
for value in range(1, 5):
    range_output = f"range position {value}"
    print(range_output)
# end for
print("print range in list format")
list_range_output = list(range(1, 5))
print(list_range_output)
print()

print("test range print from 1 to 6")
for value in range(1,6):
    range_output = f"range position {value}"
    print(range_output)
# end for
print("print range in list format")
list_range_output = list(range(1, 6))
print(list_range_output)
print()

print("test range print from 0 to 6")
for value in range(6):
    range_output = f"range position {value}"
    print(range_output)
# end for
print("print range in list format")
list_range_output = list(range(6))
print(list_range_output)
print()

print("test print range step by 2")
for value in range(2, 11, 2):
    range_output = f"range position {value}"
    print(range_output)
# end for
print("print range in list format")
list_range_output = list(range(2, 11, 2))
print(list_range_output)
print()
