"""
module name: ex_8_14_cars.py

description:
    Builds cars and stores them in a dictionary data structure for futher
    development. It will take an arbitrary number of car attributes, 
    (e.g. manufacturer, model, color, etc.), and store them as key-value pairs.

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
from pathlib import Path
from datetime import datetime
from ch8.ch8_fun_library import build_vehicle

def print_vehicle_data(vehicle_data: dict[str, str]):
    """
    Prints the vehicle data collected in the dictionary sorted by the keys

    args:
        vehicle_data: dictionary to be printed to the display

    returns:
        None

    raises:
        IndexError: If an out of range dictionary index is reached

        ValueError: If an unexpected value is encountered
    """
    try:
        for key, value in sorted(vehicle_data.items(), key=lambda item: item[0]):
            print(f"key -> {key}, value -> {value}")
        # end for
    except IndexError as e:
        print(
            f"!!!!!Sorry, but an unexpected dictionary index was encountered, "
            f"{e}!!!!!"
        ) # end print()
    except ValueError as e:
        print(
            f"!!!!!Sorry, but an unexpected value was encountered, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!Sorry, an unexpected, unhandled exception was raised, "
            f"{e}!!!!!"
        ) # end print()
    # try...except
# end print_vehicle_data()

########################
# Main app starts here #
########################
todays_datetime = datetime.now()
date_only = todays_datetime.strftime("%Y-%m-%d")
time_only = todays_datetime.strftime("%H:%M:%S")
print(
    f"**********Testing build_vehicle() on {date_only} at "
    f"{time_only}**********"
) # end print()
vehicle_status_file = (
    Path(".") / "data" / "out_files" / f"vehicle_statuses_{date_only}"
) # end vehicle_status_file
with open(vehicle_status_file, 'w', encoding='utf-8') as out_file:
    out_file.write(
        "process_date,process_time,vehicle_type,vehicle_manufacturer,"
        "vehicle_model,vehicle_attr\n"
    ) # end write()

    honda_car_dict = (
        build_vehicle('car', 'honda', 'accord', location='ca', year='2011',
                      mileage='177,655', accidents='y'
        ) # end build_vehicle()
    ) # end honda_car_dict

    print_vehicle_data(honda_car_dict)
    out_file.write(
        f"{date_only},{time_only},car,honda,accord,ca|2011|177655|y\n"
    ) # end write()
# end with