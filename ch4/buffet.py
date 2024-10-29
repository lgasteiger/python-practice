import time

def test_tuple_item_update(tuple_to_test, index, new_val):
    """this function will test the attempt to update a tuple item"""
    try: 
        tuple_to_test[3] = 'rodeo burger'
        return True
    except Exception as e:
        output_message = (
            f"!!!!!an error occurred when attempting to update the " +
            f"tuple: {e}!!!!!"
        ) # end output_message fstring
        print(output_message)
        return False
# end test_updating_tuple_item

def print_data_struct_items(data_struc_to_print):
    """this function will all the elements in data_struc_to_print"""
    try:
        for index, elem in enumerate(data_struc_to_print):
            output_message = (
                f"at index {index}, element = '{elem}'"
            ) # end output_message fstring
            print(output_message)
        # end for
        return True
    except IndexError:
        print("!!!!!IndexError: index out of range!!!!!")
        return False
    except Exception as e:
        output_message = (
            f"!!!!!an unexpected error occurred: {e}"
        ) # end output_message fstring
        print(output_message)
        return False
# end print_data_struct_items
    
def print_func_status(func_name, is_func_successful):
    """this function prints the successful/unsuccessful status of \ 
    func_name"""
    if is_func_successful:
        output_message = (
            "the function 'print_data_struct_items' completed successfully\n"
        ) # end output_message string
        print(output_message)
    else:
        output_message = (
            "!!!!!the function 'print_data_struct_items' did NOT complete " +
            "successfully!!!!!\n"
        ) # end output_message string
        print(output_message)
# end print_func_status
        
def print_perf_time(begin_time, finish_time):
    """this function prints the time it takes to complete the task(s)"""
    time_taken = begin_time - finish_time
    output_message = (
        f"the time it took in seconds to complete the task = {time_taken} " +
        f"seconds\n"
    ) # end output_message fstring
    print(output_message)
# end print_perf_time

############################
# main program starts here #
############################
start_time = time.time()
buffet_foods = (
    'tacos', 'burritos', 'greek salads', 'cheeseburgers', 'onion rings'
) # end buffet_foods tuple

print("*****the original buffet menu*****")
func_status = print_data_struct_items(buffet_foods)
print_func_status('print_data_struc_items', func_status)
end_time = time.time()
print_perf_time(start_time, end_time)

# test trying to update an item value in an immutable tuple
start_time = time.time()
func_status = test_tuple_item_update(buffet_foods, 3, 'rodeo burger')
print_func_status('test_tuple_item_update', func_status)
end_time = time.time()
print_perf_time(start_time, end_time)

# test attempting to update the entire buffet menu
start_time = time.time()
buffet_foods = (
    'pizza', 'garden salad', 'fried rice', 'tacos', 'mexican pizza'
) # end buffet_foods tuple
print("*****modified buffet menu*****")
func_status = print_data_struct_items(buffet_foods)
print_func_status('print_data_struct_items', func_status)
end_time = time.time()
print_perf_time(start_time, end_time)
