import time

def test_equality_equals(local_ip):
    """
    this function tests equality with strings
    """
    if local_ip != "" and local_ip.isspace() != True:
        local_ip_trimmed = local_ip.strip()
        if local_ip_trimmed == "10.10.56.71":
            print(
                f"yes, the '{local_ip}' is the correct isp in the local " +
                f"municipality"
            ) # end print()
        else:
            raise ValueError(
                f"no, sorry the '{local_ip}' is not recognized as the " + 
                f"correct local isp in this municipality"
        ) # end ValueError exception
        # end if
    else:
        raise ValueError(
            f"!!!!!the local ip can not be empty. please try again!!!!!"
        ) # end ValueError() exception
    # end if
# end test_equality_equals(local_ip)

def test_equality_contains(local_isp):
    """
    this function checks if one string contains another string
    """
    my_local_isp = "comcast xfinity"
    if local_isp != "" and local_isp.isspace() != True:
        local_isp_trimmed = local_isp.strip()
        local_isp_lowercase = local_isp_trimmed.lower()
        if local_isp_lowercase in my_local_isp:
            print(
                f"yes, your '{local_isp}' local isp matches your " +
                f"existing geographic location"
            ) # print()
        else:
            raise ValueError(
                f"no, the '{local_isp}' isp provider does not " + 
                f"match your current geographic area"
            ) # end ValueError exception
        # end if
    else:
        raise ValueError(
            f"!!!!!the local isp value can not be empty. please try again!!!!!"
        ) # end ValueError exception
    # end if
# end test_equality_contains(local_isp)

def test_inequality_not_equals(num_test):
    """
    this function tests inequality between numeric values
    """
    if isinstance(num_test, (int, float)):
        if num_test != 49:
            raise ValueError(
                f"sorry, the value '{num_test}' is not correct. please try " +
                f"again"
            ) # end ValueError exception
        else:
            print(
                f"great, the value '{num_test}' matches the hard coded value"
            ) # end print()
        # end if
    else:
        raise TypeError(
            f"!!!!!the '{num_test}' value is non-numeric. please try again!!!!!"
        ) # end TypeError exception
    # end if
# end test_inequality_not_equals(num_test)
    
def test_numeric_operators(num_test, math_oper):
    """
    this function tests the >, >=, <, <= operators
    """
    val_tester = 49
    if isinstance(num_test, (int, float)):
        if math_oper == ">":
            if num_test > val_tester:
                print(
                    f"the '{num_test}' value is greater than '{val_tester}'"
                ) # end print()
            else:
                print(
                    f"the '{num_test}' value is actually less than " +
                    f"'{val_tester}'"
                ) # end print()
            # end if
        elif math_oper == ">=":
            if num_test >= val_tester:
                print(
                    f"the '{num_test}' value is greater than or equal to " +
                    f"'{val_tester}'"
                ) # end print()
            else:
                print(
                    f"the '{num_test}' value is actually less than " +
                    f"'{val_tester}'"
                ) # end print()
            # end if
        elif math_oper == "<":
            if num_test < val_tester:
                print(
                    f"the '{num_test}' value is less than '{val_tester}'"
                ) # end print()
            else:
                print(
                    f"the '{num_test}' value is actualy greater than " +
                    f"'{val_tester}'"
                ) # end print()
            # end if
        elif math_oper == "<=":
            if num_test <= val_tester:
                print(
                    f"the '{num_test}' value is less than or equal to " +
                    f"'{val_tester}'"
                ) # end print()
            else:
                print(
                    f"the '{num_test}' value is actualy greater than " +
                    f"'{val_tester}'"
                ) # end print()
            # end if
        else: # raise ValueError exception
            raise ValueError(
                f"!!!!!the '{math_oper}' is not one of the recognized math " +
                f"operators. please try again!!!!!"
            ) # end ValueError exception
    else:
        raise TypeError(
            f"!!!!!the '{num_test}' is not a numeric type, please try " +
            f"again!!!!!"
        ) # end TypeError
    # end if
# end test_numeric_operators(num_test, math_oper)

def test_and_oper(first_name, last_name):
    """
    this function validates whether both the 'first_name' and 'last_name' are
    empty. if either the 'first_name' or 'last_name" or both are empty, the
    user must try again
    """
    if first_name != "" and last_name != "":
        fname_trimmed = first_name.strip()
        lname_trimmed = last_name.strip()
        if fname_trimmed.isalnum() and lname_trimmed.isalnum():
            print(
                f"great, the 'first_name' value is '{fname_trimmed.title()}' " +
                f"and 'last_name' value is '{lname_trimmed.title()}'"
            ) # end print()
        else:
            raise ValueError(
                f"!!!!!the 'first_name' and 'last_name' values cannot be " +
                f"empty or contain special characters. please try again!!!!!"
            ) # end ValueError() exception
    else:
        raise ValueError(
            f"!!!!!the 'first_name' and 'last_name' values cannot be empty. " +
            f"please provide both the 'first_name' and 'last_name' values " +
            f"and try again!!!!!"
        ) # end print()
    # end if
# end test_and_oper(first_name, last_name)
    
def test_or_oper(first_name, last_name):
    """
    this function validates that either the 'first_name' or 'last_name' values
    are not empty. if both the 'first_name' and 'last_name' are empty, then
    the user must try again 
    """
    if first_name or last_name != "":
        fname_trimmed = first_name.strip()
        lname_trimmed = last_name.strip()
        if fname_trimmed.isalnum() or lname_trimmed.isalnum():
            print(
                f"okay, 'first_name' value is '{first_name.title()}', and " + 
                f"'last_name' value is '{last_name.title()}'"
            ) # end print()
        else:
            raise ValueError(
                f"!!!!!both the 'first name' and 'last name' values are " +
                f"empty. please try again and enter values for the first " +
                f"name and last name"
            ) # end ValueError() exception
        # end if
    else:
        raise ValueError(
            f"!!!!!both the 'first name' and 'last name' values are empty. " +
            f"please try again and enter values for the first name and last " +
            f"name!!!!!"
        ) # end ValueError() exception
    # end if
# end test_or_oper(first_name, last_name)
    
def test_in_list(list_of_tabs, tablet_name):
    """
    tests whether an item is in a list
    """
    if not list_of_tabs:
        raise ValueError(
            f"!!!!!the list is empty. please try again!!!!!"
        ) # end ValueError exception
    #end if
    
    if tablet_name == "" or tablet_name.isspace():
        raise ValueError(
            f"!!!!!the tablet name value is blank or missing. please try " +
            f"again!!!!!"
        ) # end ValueError exception
    # end if
    
    tablet_name_trimmed = tablet_name.strip()
    tablet_name_trim_lower = tablet_name_trimmed.lower()
    if tablet_name_trim_lower in list_of_tabs:
        print(
            f"good news, the '{tablet_name_trim_lower.title()}' element exists " +
            f"in the list"
        ) # end print()
    else:
        print(
            f"no, sorry, the '{tablet_name_trim_lower.title()}' element is " +
            f"NOT an item in list"
        ) # end print()
    # end if
# end test_in_list(list_of_tabs, tablet_name)
        
def test_not_in_list(my_stores, find_store):
    """
    this function tests if a specific store exists in my list of stores
    """
    if not my_stores:
        raise ValueError(
            f"!!!!!the concomitant list is empty. please try again!!!!!"
        ) # end ValueError() exception
    # end if
        
    if find_store == "" or find_store.isspace():
        raise ValueError(
            f"!!!!!the store value is blank or missing. please try again!!!!!"
        ) # end ValueError() exception
    # end if

    if find_store not in my_stores:
        print(
            f"okay, we've confirmed that the '{find_store}' value does not " +
            f"currently exist in the list"
        ) # end print()
    else:
        print(
            f"we validated that the '{find_store}' values still exists " +
            f"in the list"
        ) # end print()
    # end if
# end test_not_in_list(my_stores, find_store)

#######################################################################
#                            app starts here                          #
#######################################################################

#############################
# test equality with equals #
#############################
print("*****test equality with equals operator*****")
my_ip = "10.10.56.71"
# my_ip = "  "
start_time = time.time()
try:
    test_equality_equals(my_ip)
except ValueError as e:
    print(e)
except Exception as e:
    print(
        f"!!!!!there was an unexpected, unhandled exception that occurred, "
        f"{e}!!!!!"
    ) # end print()
# end try...catch
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the time in seconds it took the function to complete was " +
    f"{elapsed_time} sec\n"
) # end print()

###############################
# test equality with contains #
###############################
print("*****test equality with contains*****")
my_isp = "Comcast Xfinity"
# my_isp = "xFinity"
# my_isp = " "
start_time = time.time()
try:
    test_equality_contains(my_isp)
except ValueError as e:
    print(e)
except Exception as e:
    print(
        f"!!!!!an unexpected, unhandled exception occcurred, {e}!!!!!"
    ) # end print()
# end try...catch
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the approximate time in seconds for the function to return was: " +
    f"{elapsed_time} sec\n"
) # end print()

###################################
# test inequality with not equals #
###################################
print("*****test inequality with not equals*****")
# test_num = "    "
# test_num = 49
test_num = 49.1
start_time = time.time()
try:
    test_inequality_not_equals(test_num)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(
        f"!!!!!there was an unexpected, unhandled exception raised, {e}!!!!!"
    ) # end print()
# end try...catch
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the approximate time in seconds it took the function to complete was: " +
    f"{elapsed_time} sec\n"
) # end print()

#######################
# test math operators #
#######################
print("*****test math operators*****")
test_val = 49
# test_val = 79
# test_val = " "
# test_val = ""
test_oper = ">="
start_time = time.time()
try:
    test_numeric_operators(test_val, test_oper)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(
        f"!!!!!an unexpected, unhandled exception occurred, {e}!!!!!"
    ) # end print()
# end try...catch
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the time in took for the function to complete and return was, " +
    f"{elapsed_time} sec\n"
) # end print()

###################################
# test 'and' conditional operator #
###################################
print("*****test 'and' conditional operator*****")
fname_value = "luke   "
lname_value = "  lucky"
start_time = time.time()
try:
    test_and_oper(fname_value, lname_value)
except ValueError as e:
    print(e)
except Exception as e:
    print(
        f"!!!!!an unexpected, unhandled exception occurred; {e}!!!!!"
    ) # end print()
# end try...except
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the amount of time it took the function to return was '{elapsed_time}' " +
    f"seconds\n"
)# end print()

##################################
# test 'or' conditional operator #
##################################
print("*****tests the 'or' conditional operator*****")
# fname_test = "pepper"
# lname_test = "lana"
fname_test = ""
lname_test = " "
start_time = time.time()
try:
    test_or_oper(fname_test, lname_test)
except ValueError as e:
    print(e)
except Exception as e:
    f"!!!!!there was an unexpected, unhandled exception that occurred, {e}"
# end try...catch
end_time = time.time()
elapsed_time = time.time()
print(
    f"the elapsed time, in seconds, it took for the function to return was, " +
    f"{elapsed_time} sec\n"
) # end print()

######################################
# tests whether an item is in a list #
######################################
print("*****tests whether an item is in a list*****")
tablet_models = [
    'samsung galaxy a9+', 'lenovo 11', 'pixel 9 tab', 'samsung galaxy s7',
    'samsung galaxy a8', 'kindle 2024', 'paper white 2024'
] # end tablet_models[]
# search_item = "Samsung Galaxy S7"
search_item = "kindle 2023"
start_time = time.time()
try:
    test_in_list(tablet_models, search_item)
except ValueError as e:
    print(e)
except Exception as e:
    f"!!!!!an unexpected, unhandled exception was raised, {e}!!!!!"
# end try...except
end_time = time.time()
elapsed_time = time.time()
print(
    f"the time in seconds it took for the function to complete sequentially " +
    f"and return to main process was, {elapsed_time} sec\n"
) # end print()

####################################
# test if an item is not in a list #
####################################
print("*****test if an item is not in a list*****")
store_names = [
    'walmart', 'target', 'amazon', 'dicks sporting goods', 'veterans',
    'walgreens'
] # end store_names[]
# store_find = ""
# store_find = " "
# store_find = "cvs"
store_find = "amazon"
start_time = time.time()
try:
    test_not_in_list(store_names, store_find)
except ValueError as e:
    print(e)
except Exception as e:
    print(
        f"!!!!!an unexpected, unhandle exception was raised, {e}!!!!!"
    ) # end print()
# end try...except
end_time = time.time()
elapsed_time = end_time - start_time
print(
    f"the time in seconds to complete the function and return was, "
    f"'{elapsed_time}' sec"
) # end print()
