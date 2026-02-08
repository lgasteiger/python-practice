"""
module name: ch7_5_movie_tickets.py

description:
    prompts the user for their age and tells them the cost of their ticket

author: L g
created: 2026-02-02
last modified: 2026-02-04
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

from ch6.ch6_fun_library import get_valid_input, is_continue
from ch7.ch7_fun_library import get_natural_num_input

def process_tickets():
    """
    calculates ticket prices depending on a person's age. if a person is under
    the age of 3, then the cost of the is 0. if the person is betw the ages of 3
    and 12, then the cost of the ticket is $10. if the person is over 12 years
    of age, then the cost of the ticket is $15.
    """
    while True:
        patron_age = get_natural_num_input("please enter your age: ")
        if patron_age is not None:
            if patron_age < 3:
                print(
                    f"the cost of the ticket for someone \"{patron_age}\" " 
                    f"years old is: $0\n"
                ) # end print()
            # end if
                
            if patron_age >= 3 and patron_age <= 12:
                print(
                    f"the cost of the ticket for someone \"{patron_age}\" "
                    f"years old is: $10\n"
                ) # end print()
            # end if
                
            if patron_age > 12:
                print(
                    f"the cost of the ticket for someone \"{patron_age}\" "
                    f"yease old is: $15\n"
                ) # end print()
            # end if
        # end if
            
        if not is_continue():
            break
        # end if
    # end while
# end process_ticket()

########################
# main app starts here #
########################
process_tickets()
