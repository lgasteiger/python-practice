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
from ch6.ch6_fun_library import print_dict_elem

def build_vehicle(
        type: str, manufacturer: str, model: str, **vehicle_info: dict[str, str]
    ) -> dict[str, str]:
    """
    Returns a dictionary of car key/value pairs of car data.

    args:
        type: str is the type of vehicle the vehicle is

        manufacturer: str is the manufacturer name of the vehicle

        model: str is the model name of the vehicle

        **car_info: dict[str, str] is the arbitrary number of dictionary 
        key/value pairs of vehicle data

    returns:
        dict[str, str]: dictionary of vehicle key/value pairs data

    raise:
        FileNotFoundError: raises an exception if the file path can not be
        resolved

        IOError: raises an exception if vehicle status data can not be written
        to an output file
    """
    try:
        vehicle_info['type'] = type
        vehicle_info['manufacturer'] = manufacturer
        vehicle_info['model'] = model
        return vehicle_info
    except FileNotFoundError as e:
        print(
            f"!!!!!Sorry, but the output file path could not be resolved, "
            f"{e}!!!!!"
        ) # end print()
    except IOError as e:
        print(
            f"!!!!!Sorry, but an IOError exception was raised because an "
            f"error was thrown when writting to the output file, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!Sorry, an unhandled, unexpected exception was raised, "
            f"{e}!!!!!"
        ) # end print()
    # end try...except
# end build_car()

########################
# Main app starts here #
########################
todays_datetime = datetime.now()
date_only = todays_datetime.strftime("%Y-%m-%d")
time_only = todays_datetime.strftime("%H:%M:%S")
print(f"Testing build_vehicle() on {date_only} at {time_only}")
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

    print_dict_elem(honda_car_dict)
    out_file.write(
        f"{date_only},{time_only},car,honda,accord,ca|2011|177655|y\n"
    ) # end write()
# end with