def test_print_list(output_list, appended_string=""):
    """"tests printing a custom list of items"""
    for index, item in enumerate(output_list):
        if is_numeric(item):
            output_message = f"{index + 1}. {item}{appended_string}"
        else:
            output_message = f"{index + 1}. {item.title()}{appended_string}"
        # end if
        
        print(output_message)
    # end for
# end test_print_list(output_list, appended_string="")

def test_get_list_item(existing_list, index_num):
    """tests indexing custom list of items"""
    return existing_list[index_num]
# end test_get_list_item(existing_list, index_num)

def test_update_list_item(existing_list, index_num, item_update):
    """tests updating a specific list item"""
    existing_list[index_num] = item_update
# end test_update_list_item(existing_list, index_num)
    
def is_numeric(value):
    """checks if value is either an int, float, or complex number"""
    return isinstance(value, (int, float, complex))
# end is_numeric(value)

def test_add_list_item(existing_list, location, new_item):
    """tests adding a new list item at location in existing_list"""
    # tests if location is numeric. if numeric, then add new_item at location 
    # index in existing_list. otherwise, add new item at location top, end, or
    # middle of existing_list.
    if is_numeric(location):
        existing_list.insert(location, new_item)
    else:
        formatted_loc = location.lower() 
        if formatted_loc == "top":
            existing_list.append(new_item)
        elif formatted_loc == "middle":
            mid_idx = round(len(existing_list) / 2)
            existing_list.insert(mid_idx, new_item)
        elif formatted_loc == "bottom":
            existing_list.insert(0, new_item)
        else:
            print(f"!!!!!{location} is not a valid location value!!!!!")
    # end if
# end test_add_list_item()
    
def test_remove_list_item(existing_list, location):
    """tests deleting existing list item at location index in existing_list"""
    # tests if location is numeric, if numeric, then item at location is removed
    # from existing_list. otherwise, removes item at location top, end, or
    # middle of existing_list.
    if is_numeric(location):
        del_val = existing_list.pop(location)
    else:
        lower_case_loc = location.lower()
        if lower_case_loc == "top":
            del_val = existing_list.pop()
        elif lower_case_loc == "middle":
            mid_idx = round(len(existing_list) / 2)
            del_val = existing_list.pop(mid_idx)
        elif lower_case_loc == "bottom":
            del_val = existing_list.pop(0)
        else:
            del_val = f"!!!!!{location} is not a valid location value!!!!!"
    # end if
            
    return del_val
# end test_remove_list_item(existing_list, location)

def test_remove_list_item_value(existing_list, del_value):
    existing_list.remove(del_value)
# end test_remove_list_item_value(existing_list, del_value)

def test_sort_list(existing_list, is_sort_perm, is_descending=False):
    """tests sorts existing_list permanently or temporarily and ascending or descending"""
    if is_sort_perm == True:
        existing_list.sort(reverse=is_descending)
    else:
        sorted_list = sorted(existing_list, reverse=is_descending)
        print("here is the sorted list:")
        test_print_list(sorted_list)
    # end if
# end test_sort_list(existing_list, is_sort_permanent, is_ascending=True)
    
def test_print_list_reversed(existing_list):
    """tests the printing of the existing_list in reversed order"""
# end test_print_list_reversed(existing_list)
    
def test_print_list_length(existing_list):
    """tests the printing of the number of existing_list items"""
# end test_print_list_length(existing_list)
    
def test_print_range(end, start=0):
    """tests the printing of a range of numbers from start to end - 1"""
    print("**remember the range will print only until end - 1")
    for value in range(start, end):
        range_output = f"range position {value}"
        print(range_output)
    # end for
# end test_print_range(start, end)
