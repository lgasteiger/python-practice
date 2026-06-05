"""
module name: ex_8_2_favorite_book.py

description:
    displays a message to the screen depicting one of the users's favorite
    books

author: L g
created: 2026-05-21
last modified: 2026-05-21
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""
from ch6.ch6_fun_library import is_continue
from ch8.ch8_fun_library import ex_8_2_display_fav_book, ex_8_2_get_favorite_book

########################
# main app starts here #
########################
while True:
    fav_book_response = ex_8_2_get_favorite_book()
    ex_8_2_display_fav_book(fav_book_response)

    if not is_continue():
        break
    # end if
# end while
