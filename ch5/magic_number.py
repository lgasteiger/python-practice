import time

def is_correct_num(num, comp_oper):
    """
    this function confirms whether the correct number was received. a TypeError
    exception is raised when a non-numeric value is assigned the "num" var.
    a ValueError exception is raised if an invalid mathematical operator is
    assigned to the "comp_oper" var in type string 
    """
    if isinstance(num, int):
        if comp_oper == '!=':
            if num != 42:
                print_message = (
                    f"!!!!!sorry, '{num}' is not the correct answer. " +
                    f"please try again!!!!!"
                ) # end print_message
            else:
                print_message = (
                    f"yes, '{num}' is the correct answer. thank you for " +
                    f"your assistance"
                ) # end print_message
            # end if
            print(print_message)
        elif comp_oper == '<':
            if num < 21:
                print_message = (
                    f"the value '{num}' is less than 21"
                ) # end print_message
            else:
                print_message = (
                    f"the value '{num}' is greater than 21"
                ) # end print_message
            # end if
            print(print_message)
        elif comp_oper == '<=':
            if num <= 21:
                print_message = (
                    f"the value '{num}' is less than or equal to 21"
                ) # end print_message
            else:
                print_message = (
                    f"the value '{num}' is greater than than 21"
                ) # end print_message
            # end if
            print(print_message)
        elif comp_oper == '>':
            if num > 21:
                print_message = (
                    f"the value '{num}' is greater than than 21"
                ) # end print_message
            else:
                print_message = (
                    f"the value '{num}' is less than 21"
                ) # end print_message
            # end if
            print(print_message)
        elif comp_oper == '>=':
            if num >= 21:
                print_message = (
                    f"the value '{num}' is greater than than or equal to " +
                    f"21"
                ) # end print_message
            else:
                print_message = (
                    f"the value '{num}' is less than 21"
                ) # end print_message
            # end if
            print(print_message)
        else: 
            raise ValueError(
                f"!!!!!the {comp_oper} value is invalid and caused a "
                f"ValueError exception. please try again!!!!!\n"
            ) # end ValueError exception
        # end if
    else:
        raise TypeError (
            f"!!!!!the '{num}' value is non-numeric and caused a TypeError "
            f"exception. please try again!!!!!\n"
        ) # end TypeError exception
    # end if
# end is_correct_num(num, comp_oper)

def test_is_correct_num(num, math_oper):
    """
    this function tests the existing test use cases and prints the time it
    takes to complete the test use case. if a TypeError, ValueError, or 
    generic exception is raised, the concomitant TypeError, ValueError, or
    generic error message is printed to the display. 
    """
    try:
        start_time = time.time()
        is_correct_num(num, math_oper)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print_message = (
            f"!!!!!an unexpected exception error occurred, {e}!!!!!\n"
        )
        print(print_message)
    # end try...except
    
    end_time = time.time()
    elapsed_time = start_time - end_time
    print_message = (
        f"the time in seconds it took to complete all processes was " +
        f"{elapsed_time} seconds\n"
    ) # end print_message
    print(print_message)
# end test_is_correct_num(num, math_oper)
        
def is_correct_age(person_age_0, person_age_1):
    """
    this function verifies that both the "person_age_0" and "person_age_1"
    arguments are values over 21. a TypeError exception is raised
    when either "person_age_0" or "person_age_1") is not an int. a generic
    exception is raised when an unexpected exception is raised.
    """
    if isinstance(person_age_0, int) and isinstance(person_age_1, int):
        if person_age_1 >= 21 and person_age_1 >= 21:
           print_message = (
                f"the age '{person_age_1}' and age '{person_age_1}' are both " +
                f"over the age of 21"
            ) # end print_message
           print(print_message)
        else:
            raise ValueError(
                f"sorry, either '{person_age_0}' or '{person_age_1}' is " +
                f"not over the age of 21. please try again"
            ) # end ValueError exception
        # end if
    else:
        raise TypeError(
                f"!!!!!one or both ages, '{person_age_0}' and "
                f"'{person_age_1}' is not a valid int!!!!!"
            ) # end TypeError exception
    # end if
# end is_correct_age(person_age_0, person_age_1)
        
def test_is_correct_age(test_age_0, test_age_1):
    """
    this function tests the use cases for the is_correct_age() function
    """
    try:
        start_time = time.time()
        is_correct_age(test_age_0, test_age_1)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print_message = (
            f"!!!!!an unexpected exception error occurred, {e}!!!!!\n"
        ) # end print_message
        print(print_message)
    # end try...catch
        
    end_time = time.time()
    elapsed_time = end_time - start_time
    print_message = (
        f"the time in seconds it took to complete all processes was " +
        f"{elapsed_time} seconds\n"
    ) # end print_message
    print(print_message)
# end test_is_correct_age(test_age_0, test_age_1)

def is_valid_age(p_age_0, p_age_1):
    """
    this function test whether the p_age_0 or p_age_1 arguments is over the 
    value 21. if either p_age_0 or p_age_1 is not an int, then a TypeError 
    exception is raised. moreover, if either p_age_0 or p_age_1 parameters is
    not over 21, then a ValueError exception is raised 
    """
    if isinstance(p_age_0, int) and isinstance(p_age_1, int):
        if p_age_0 >= 21 or p_age_1 >= 21:
            print_message = (
                f"great news! either '{p_age_0}' or '{p_age_1}' is over 21"
            ) # end print_message
            print(print_message)
        else:
            raise ValueError(
                f"sorry, both '{p_age_0}' and '{p_age_1}' are not 21"
            ) # end ValueError exception
    else:
        raise TypeError(
            f"!!!!!either '{p_age_0}' or '{p_age_1} is not an int. please " +
            f"try again!!!!!"
        ) # end TypeError exception
    # end if
# end is_valid_age(p_age_0, p_age_1)
    
def test_is_valid_age(test_a_0, test_a_1):
    """tests is_valid_age() with the prescribed test cases"""
    try:
        start_time = time.time()
        is_valid_age(test_a_0, test_a_1)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print_message = (
            f"!!!!!an unexpected exception error occurred, {e}!!!!!\n"
        ) # end print_message
        print(print_message)
    # end try...except
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print_message = (
        f"the time in seconds it took to complete all processes was " +
        f"{elapsed_time} seconds\n"
    ) # end print_message
    print(print_message)
# end test_is_valid_age(test_a_0, test_a_1)

###################
# app starts here #
###################
print("**********test case 1**********")
answer = 17
str_operator = "!="
test_is_correct_num(answer, str_operator)

print("**********test case 2**********")
answer = 19
str_operator = "<"
test_is_correct_num(answer, str_operator)

print("**********test case 3**********")
str_operator = "<="
test_is_correct_num(answer, str_operator)

print("**********test case 4**********")
str_operator = ">"
test_is_correct_num(answer, str_operator)

print("**********test case 5**********")
str_operator = ">="
test_is_correct_num(answer, str_operator)

print("**********test case 6**********")
age_0 = 22
age_1 = 18
test_is_correct_age(age_0, age_1)

print("**********test case 7**********")
start_time = time.time()
age_1 = "xyz"
test_is_correct_age(age_0, age_1)

print("**********test case 8**********")
start_time = time.time()
age_1 = 18
test_is_valid_age(age_0, age_1)

print("##########test case 9**********")
age_0 = 18
test_is_valid_age(age_0, age_1)
