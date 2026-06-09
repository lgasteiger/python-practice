"""
module name: ex_8_7_music_album.py

description:
    prompts for an artist name and concomitant album and builds a dictionary
    of musicians and their work.

author: L g
created: 2026-06-5
last modified: 2026-06-05
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""
from ch6.ch6_fun_library import is_continue, print_dict_elem
from ch8.ch8_fun_library import ex_8_7_make_album, greet_users, print_models
from ch8.ch8_fun_library import show_completed_models

########################
# main app starts here #
########################
print("**********testing making an album**********")
while True:
    print_dict_elem(ex_8_7_make_album())

    if not is_continue():
        break
    # end if
# end while
print()

print("**********testing user greeting**********")
usernames = ['hanna', 'ty', 'margot']
greet_users(usernames)
print()

print("**********testing updating a list data structure**********")
unprinted_designs_list = ['phone case', 'robot pendant', 'dodecahedron']
printed_design_list = print_models(unprinted_designs_list)
show_completed_models(printed_design_list)
