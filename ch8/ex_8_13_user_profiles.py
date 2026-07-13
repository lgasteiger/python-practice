"""
module name: ex_8_13_user_profiles.py

description:
    Processes student applications from an input file and prints the status
    of the application to the display and an output file.

author: L G Gasteiger
created: 2026-07-13
last modified: 2026-07-13
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module is an example from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""
from datetime import datetime
from pathlib import Path
from ch8.ch8_fun_library import build_profile

########################
# Main app starts here #
########################
todays_datetime = datetime.now()
date_only = todays_datetime.strftime("%Y-%m-%d")
time_only = todays_datetime.strftime("%H:%M:%S")
print(
    f"**********Testing build_profile() on {date_only} at {time_only}**********"
) # end print()
completed_orders_file = (
    Path(".") / "data" / "input_files" / f"student_data_2026_07-13.csv"
) # end completed_orders_file
build_profile(completed_orders_file)
