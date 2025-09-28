import ch6_fun_library

"""
filename: ch6-3_exercise.py

author: gasteiger, L g
date: 2025-09-06
"""

def is_continue():
    """
    this function prompts the user if they wish to continue. if the input
    response from the user is 'y' or 'Y', then the app will continue.
    otherwise, the app will end
    """
    try:
        while True:
            user_response = input(
                 "would you like to continue entering programming topics? (y/n) "
            ) # end input()

            if user_response == "":
                print(
                    "!!!!!please enter an input. the input cannot be blank!!!!!"
                ) # end print()
            elif user_response == "y" or user_response == "Y":
                return True
            else:
                return False
            # end if
        # end while
    except ValueError as e:
        print(f"!!!!!a ValueError occured, {e}!!!!!")
    except Exception as e:
        print(f"!!!!!an unexpected error occurred, {e}!!!!!")
    # end try...except
    # end while
# end is_continue()

def get_new_prog_concept():
    """
    this function prompts for new key/value pair(s) of programming topics
    and definitions. 
    """
    try:
        while True:
            user_input = input(
                "please enter the recently learned programming concept and definition: "
            ) # end input()

            if user_input == "":
                print(
                    "!!!!!sorry, no value was recorded as input. value can not be blank!!!!!"
                ) # end print()
            else:
                sanitized_input = user_input.strip().lower().split(':')
                break
            # end if
        # end while
    
        return sanitized_input
    except Exception as e:
        print(f"!!!!!an unexpected error occurred, {e}!!!!!")
    # end try...except
# end get_new_prog_concept()

def add_new_prog_concept(gloss_dict, new_sw_topic):
    """
    this function will add a new key/value pair of software programming
    concept to the gloss_dict dictionary data structure
    """
    try:
        sw_topic_key = new_sw_topic[0].strip()
        sw_topic_value = new_sw_topic[1].strip()
        gloss_dict[sw_topic_key] = sw_topic_value
    except IndexError as e:
        print(
            f"!!!!!!there was an index out of range or invalid list index, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(f"!!!!!an unexpected error occurred, {e}!!!!!")
    # end try...except
# end add_new_prog_concept()
    
def process_new_prog_concepts(upd_glossary_dict):
    """
    this function will receive input from the keyboard for new programming
    topics and add them to the upd_glossary_dict dictionary data structure
    until the user explicitly wants to quit the app. if the input is blank, 
    the app will loop through until an input value is entered.
    """
    while True:
        new_prog_concept = get_new_prog_concept()
        add_new_prog_concept(glossary_dict, new_prog_concept)
        if not is_continue():
            break
        # end if
    # end while
# end process_new_prog_concepts()

###############################
# main program starting point #
###############################
glossary_dict = {
    "kotlin": "multi-platform programming",
    "swiftui": "mobile dev ios apple",
    "python 3": "current ai dev platform and tools",
    "javascript": "foundational software stack for all things web",
} # end glossary_dict

print(f"*****test printing glossary dictionary*****")
ch6_fun_library.print_dict_elem(glossary_dict)
print()

print("*****testing new programming topic input from console cmd line*****")
process_new_prog_concepts(glossary_dict)
ch6_fun_library.print_dict_elem(glossary_dict)
print()
