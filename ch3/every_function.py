import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from tutorial_utils.tutorial_helpers import *

##########################################
#      the program starts here           #
##########################################
prog_languages = ['kotlin', 'javascript', 'python', 'java', 'c++', 'c']
test_print_list(prog_languages, ", is the best programming languages to learn.")
print()
test_print_list(prog_languages, " is the programming language taught in school.")
print()

print("*****tests the indexing of a custom list of items*****")
first_item = test_get_list_item(prog_languages, 0)
print(f"here is the first item of the list: {first_item}")
middle_idx = round(len(prog_languages) / 2) - 1
middle_item = test_get_list_item(prog_languages, middle_idx)
print(f"here is the middle item from the list: {middle_item}\n")

print("*****tests updating a specific list item*****")
new_item = "typescript" 
idx = 1
test_update_list_item(prog_languages, idx, new_item)
test_print_list(prog_languages)
print()

print("*****tests adding a new list item anywhere in the list, in this case top*****")
test_add_list_item(prog_languages, "top", "c#")
test_print_list(prog_languages)
print()

print("*****tests adding a new list item anywhere in the list, in this case bottom*****")
test_add_list_item(prog_languages, "bottom", "rust")
test_print_list(prog_languages)
print()

print("*****tests adding a new list item anywhere in the list, in this case middle*****")
test_add_list_item(prog_languages, "middle", "go")
test_print_list(prog_languages)
print()

print("*****retests adding a new list item by numeric location*****")
test_add_list_item(prog_languages, 5, "haskel")
test_print_list(prog_languages)
print()

print("*****tests deleting list value from a numeric idx*****")
removed_val = test_remove_list_item(prog_languages, 5)
print(f"the value removed from the list = {removed_val}")
test_print_list(prog_languages)
print()

print("*****tests removing list element from the top location*****")
removed_val = test_remove_list_item(prog_languages, "top")
print(f"the value removed from the list = {removed_val}")
test_print_list(prog_languages)
print()

print("*****tests removing list element from middle location*****")
removed_val = test_remove_list_item(prog_languages, "middle")
print(f"the value removed from the list = {removed_val}")
test_print_list(prog_languages)
print()

print("*****test removing list element from end location*****")
removed_val = test_remove_list_item(prog_languages, "end")
print(f"the value removed from the list = {removed_val}")
test_print_list(prog_languages)
print()

print("*****tests removing list element from the bottom location*****")
removed_val = test_remove_list_item(prog_languages, "bottom")
print(f"the value removed from the list = {removed_val}")
test_print_list(prog_languages)
print()

print("*****testing the removal of a list element by value name*****")
test_remove_list_item_value(prog_languages, "java")
test_print_list(prog_languages)
print()

print("*****tests sorting of a list permanently ascending*****")
test_sort_list(prog_languages, True)
test_print_list(prog_languages)
print()

print("*****tests sorting of a list permanently descending*****")
allergy_meds = ['benadryl', 'allergra', 'claratin', 'xytol', 'zertec']
test_sort_list(allergy_meds, True, True)
test_print_list(allergy_meds)
print()

print("*****tests sorting of a list temporarily in ascending order*****")
throat_drops = ['halls', 'vitamin c', 'true care', 'equate']
test_sort_list(throat_drops, False)
print("here is the original list elements:")
test_print_list(throat_drops)
print()

print("*****tests sorting of a list temporarily in descending order*****")
# cars_owned = ['nissan datsun', 'ford escort', 'ford mustang', 'honda accord', 'toyota prius']
test_sort_list(throat_drops, False, True)
print("here is the original list elements:")
test_print_list(throat_drops)
print()

print("*****tests printing a list in reversed order unsorted*****")
cars_owned = ['nissan datsun', 'ford escort', 'ford mustang', 'honda accord', 'toyota prius']
print("here is the original list:")
test_print_list(cars_owned)
cars_owned.reverse()
print("here is the list reversed:")
test_print_list(cars_owned)
print()

print("*****tests printing list length*****")
list_length = len(cars_owned)
print(f"the length of my cars owned list is: {list_length}")
print()

#test_value = "5++"
#test_value= 55
#if is_numeric(test_value):
#    print(f"the value, {test_value}, is numeric")
#else:
#    print(f"the value, {test_value} is NOT numeric")
# end if...else
