"""
module name: ex_8_9_messages.py

description:
    prints the the display a list of messages. sends a copy of the messages
    list

author: L g gasteiger
created: 2026-06-08
last modified: 2026-06-08
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""
from pathlib import Path
from ch6.ch6_fun_library import print_list_items
from ch8_fun_library import show_txt_messages, send_txt_messages

########################
# main app starts here #
########################
print("**********testing show existing text messages**********")
file_path = Path(".") / "data" / "text_messages_2026.dat"
show_txt_messages(file_path)
print()

print("***********test sending and processing text messages**********")
success_txt_messages_lst = send_txt_messages(file_path)
print_list_items(success_txt_messages_lst)
