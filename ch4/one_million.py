import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from tutorial_utils.tutorial_helpers import test_print_list

print("print the first one million sequential elements in a list")
one_million_elems = list(range(1, 1000001))
for index, elem in enumerate(one_million_elems):
    output_message = f"at list position {index}, the element is {elem}"
    print(output_message)
# end for
