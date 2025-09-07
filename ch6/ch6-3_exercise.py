import ch6_fun_library

"""
filename: ch6-3_exercise.py

author: gasteiger, L g
date: 2025-09-06
"""

def get_new_prog_concept():
    """
    this function returns the new key/value pair of the programming topic
    and definition
    """
    while True:
        user_input = input(
            "please enter the recently learned programming concept and " + 
            "definition: "
        ) # end input()

        if user_input == "":
            print(
                "!!!!!sorry, no value was recorded as input. value can not " +
                "be blank.!!!!!"
            ) # end print()
        else:
            sanitized_input = user_input.strip().lower().split(':')
            break
        # end if
    # end while
        
    return sanitized_input
# end get_new_prog_concept()

def add_new_prog_concept(gloss_dict, new_sw_topic):
    """
    this function will add a new key/value pair of software programming
    concept
    """
    sw_topic_key = new_sw_topic[0].strip()
    sw_topic_value = new_sw_topic[1].strip()
    gloss_dict[sw_topic_key] = sw_topic_value
# end add_new_prog_concept()

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
prog_concept = get_new_prog_concept()
add_new_prog_concept(glossary_dict, prog_concept)
ch6_fun_library.print_dict_elem(glossary_dict)
print()