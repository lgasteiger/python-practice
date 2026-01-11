from ch6.ch6_fun_library import get_valid_input

"""
filename: greeter.py

author: gasteiger, L g
version: 1.0
"""

############################
# main program starts here #
############################
print("**********test string input**********")
name_input = get_valid_input("please enter your name: ")
print(f"hello, {name_input.title()}\n")

prompt = "if you share your name, we can personalize the messages you see."
prompt += "\nwhat is your first name: "
name = get_valid_input(prompt)
print(f"hello, {name.title()}!\n")

print("**********test int input**********")
