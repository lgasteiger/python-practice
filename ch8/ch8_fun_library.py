"""
module name: ch8_fun_library.py

description:
    contains reusable functions originally created in the chapter 8 exercises
    of the "Python Crash Course, 3rd Ed." by Prof. Matthes, E.

author: L g
created: 2026-06-02
last modified: 2026-06-02
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module contains examples from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""
from ch6.ch6_fun_library import get_valid_input, print_list_items, is_continue
from ch6.ch6_fun_library import print_dict_elem
from pathlib import Path
from datetime import datetime
import csv

def ex_8_2_get_favorite_book():
    """
    prompts the user for one of their favorite books

    args:
        none

    returns:
        one of the user's favorite books

    raises:
        none
    """

    user_fav_book = get_valid_input(
        "please enter one of your favorite books: "
    ) # end get_valid_input()

    return user_fav_book    
# end ex_8_2_get_favorite_book()
    
def ex_8_2_display_fav_book(title):
    """
    prints to the display screen a message concerning one of the user's
    favorite books.

    args:
        title: the user's favorite book

    returns:
        none

    raises:
        none 
    """

    print(
        f"one of the user's favorite books is: '{title}'\n"
    ) # end print()
# end ex_8_2_display_fav_book()

def ex_8_3_write_shirt(size, text_message):
    """
    prints to the display a message summarizing the size of the shirt and the
    message printed on it.

    args:
        size: the size of the shirt

        text_message: the message that is to be printed on the shirt

    returns:
        none

    raises:
        none
    """
    print(
        f"the size of the shirt is '{size}', and the message to be printed on "
        f"the shirt is: '{text_message}'\n"
    ) # end print()
# end ex_ch8_3_write_shirt()
    
def ex_8_3_write_shirt2(size="L", display_message="i love python"):
    """
    prints to the display a message summarizing the size of the shirt and the
    message printed on it.

    args:
        size: the size of the shirt is default 'L'

        text_message: the message that is to be printed on the shirt is
                      default to 'i love python'

    returns:
        none

    raises:
        none
    """
    print(
        f"the size of the shirt is '{size}', and the message to be printed on "
        f"the shirt is: '{display_message}'\n"
    ) # end print()
# end ex_ch8_3_write_shirt2()
    
def ex_8_3_get_shirt_data():
    """
    prompts for shirt size and t-shirt message and accepts input from the 
    console. then, returns a dictionary with t-shirt size and message to be 
    printed on shirt.

    args:
        none

    returns:
        dictionary with t-shirt size and message printed on it

    raises:
        none 
    """
    t_shirt_dict = {}
    shirt_size = get_valid_input("please enter the size of the t-shirt: ")
    t_shirt_dict["size"] = shirt_size

    shirt_message = get_valid_input(
        "please enter the message that will be printed on the shirt: "
    ) # end get_valid_input()
    t_shirt_dict["text"] = shirt_message
    return t_shirt_dict
# end ex_ch8_3_get_shirt_data()

def ex_8_5_desc_city():
    """
    prompts for the name of a city and its country. then, the city and its
    country is printed to the display. the default country parameter value is 
    'United States'.

    args:
        none

    returns:
        none

    raises:
        none 
    """
    city_name = get_valid_input("please enter a city: ")
    country_name = get_valid_input("please enter the city's country: ")
    print(
        f"{city_name.title()} is in {country_name.title()}\n"
    ) # end print()
# ex_ch8_5_desc_city()

def get_formatted_name(first_name, last_name, middle_name=""):
    """
    returns the name neatly formatted in the format 'first_name middle_name 
    last_name'. if no middle name is provided then the format will be 
    'first_name last_name'.

    args:
        first_name: string first name provided

        last_name: string last name provided

        middle_name: string middle name provided. optional
    
    returns:
        the formatted string name

    raises:
        none
    """
    if middle_name:
        fullname = f"'{first_name} {middle_name} {last_name}'\n"
    else:
        fullname = f"'{first_name} {last_name}'\n"
    # end if
        
    return fullname.title()
# end get_formatted_name()

def make_album(name, album_title, num_of_songs=None):
    """
    returns a dictionary with the musician's name, album title and number of
    songs on the album.

    args:
        name: artist name

        album_title: artist's album title

        num_of_songs: the number of songs on the artist's album

    returns:
        dictionary of a musician's album info

    raises:
        none
    """
    music_album_dict = {
        "artist_name": name, 
        "album_name": album_title,
        "song_total": num_of_songs,
    } # end music_album_dict

    return music_album_dict
# end make_album()

def ex_8_7_make_album():
    """
    builds a dictionary describing a music album. prompts for an artist name
    and an album title from the console. then, returns a dictionary containing
    these two pieces of info.

    args:
        none

    returns:
        dictionary containing an artist name, album title, and number of 
        album songs

    raises:
        none
    """
    musician_name = get_valid_input("please enter the music artist name: ")
    lp_name = get_valid_input("please enter the name of the music album: ")
    songs_count = get_valid_input("please the number of songs on the album: ")
    return make_album(musician_name, lp_name, songs_count)
# end ex_8_7_make_album()

def greet_users(names_list):
    """
    prints a greeting to the display for each of the folks in the names list.

    args:
        names_list: list of names

    returns:
        none

    raises:
        none
    """
    for name in names_list:
        print(f"hello, {name.title()}. welcome aboard!")
    # end for
# end greet_users()
        
def print_models(design_models_list):
    """
    processes each design model, prints the status to the display, and moves
    the completed design model to a completed model list.

    args:
        design_models_list: list of design models to be processed

    returns:
        list of completed models

    raises:
        none
    """
    completed_models_list = []
    while design_models_list:
        current_design = design_models_list.pop()
        print(f"printing model: {current_design}")
        completed_models_list.append(current_design)
    # end while
        
    return completed_models_list
# end print_models()
        
def show_completed_models(models_list):
    """
    displays to the screen the list of completed models that were processed
    successfully.

    args:
        models_list: list of models to be shown on the display

    return:
        none

    raises:
        none
    """
    print_list_items(models_list)
# end show_completed_models()
    
def show_txt_messages(txt_messages_file: Path):
    """
    prints each text message to the display.

    args:
        txt_messages_file: string file path of text messages file

    returns:
        none

    raises:
        FileNotFoundError: exception raised when file is not found at the 
                           specified file path location
        IOError: exception raised when file can not be read or written to
    """
    try:
        with open(txt_messages_file, 'r', encoding='utf-8') as file:
            for line in file:
                txt_message = line.strip()
                if txt_message:
                    print(
                        f"existing text message to be transmitted: "
                        f"'{txt_message}'"
                    ) # end print()
                # end if
            # end for
    except FileNotFoundError as e:
        print(
            f"!!!!!sorry, file located at '{txt_messages_file}' is not found. "
            f"'{e}'. please try again when you get a chance!!!!!"
        ) # end print()
    except IOError as e:
        print(
            f"!!!!!sorry, an I/O error occurred, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!sorry, there was an unhandled, unexpected error that "
            f"occurred, '{e}'!!!!!"
        ) # end print()
    # end try...except
# end show_messages()
    
def send_txt_messages(txt_messages_file: Path):
    """
    processes text messages in the txt_messages_list list data structure.
    prints to the display the status of processed text message, and moves
    all successfully sent text messages to a completed text message list.

    args:
        txt_messages_list: list of text messages that need to be sent

    returns:
        list of successfully sent text messages

    raises:
        FileNotFoundError: exception raised when file is not found at the 
                           specified file path location
        IOError: exception raised when file can not be read or written to
    """
    completed_txt_messages_list = []
    try:
        with open(txt_messages_file, 'r', encoding='utf-8') as file:
            for line in file:
                curr_text_message = line.strip()
                if curr_text_message:
                    print(f"sending text message: '{curr_text_message}'")
                    completed_txt_messages_list.append(curr_text_message)
                # end if
            # end for
        # end with
    except FileNotFoundError as e:
        print(
            f"!!!!!sorry, file located at '{txt_messages_file}' is not found. "
            f"'{e}'. please try again when you get a chance!!!!!"
        ) # end print()
    except IOError as e:
        print(
            f"!!!!!sorry, an I/O error occurred, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!sorry, there was an unhandled, unexpected error that "
            f"occurred, '{e}'!!!!!"
        ) # end print()
    # end try...except

    return completed_txt_messages_list
# end send_txt_messages()

def make_pizza(pizza_toppings_file: Path):
    """
    processes pizza orders saved to a text file. displays the status to
    the screen of each pizza order. saves the completed pizza orders to a 
    completed pizza orders text file.

    args:
        pizza_toppings_file: file path of the file 

    returns:
        file path to processed pizza orders

    raises:
        FileNotFoundError: exception raised when file is not found at the 
                           specified file path location
        IOError: exception raised when file can not be read or written to
    """
    try:
        with open(pizza_toppings_file, 'r', encoding='utf-8') as input_file:
            todays_date = date.today().strftime("%Y-%m-%d")
            orders_output_file = Path(".") / "data" / f"completed_orders_from_txt{todays_date}.txt"
            with open(orders_output_file, 'w', encoding='utf-8') as output_file:
                for line in input_file:
                    curr_pizza_order = line.strip()
                    print(
                        f"completed pizza order: '{curr_pizza_order}'"
                    ) # end print()
                    output_file.write(
                        f"completed pizza order: '{curr_pizza_order}'\n"
                    ) # end write
                # end for
            # end with
        # end with
    except FileNotFoundError as e:
        print(
            f"!!!!!sorry, file located at '{pizza_toppings_file}' is not found. "
            f"'{e}'. please try again when you get a chance!!!!!"
        ) # end print()
    except IOError as e:
        print(
            f"!!!!!sorry, an I/O error occurred, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!sorry, an unexpected, unhandled exception was encountered, "
            f"{e}!!!!!"
        ) # end print()
# end make_pizza()
        
def make_pizza_v2(pizza_toppings_file: Path):
    """
    Processes pizza orders saved to a flat file delimited by a comma. 
    Displays the status to the screen of each pizza order. 
    Saves the completed pizza orders to a completed pizza orders text file.

    args:
        pizza_toppings_file: file path of the pizza toppings file for the 
                             pizza orders 

    returns:
        file path to processed pizza orders

    raises:
        FileNotFoundError: exception raised when file is not found at the 
                           specified file path location
        IOError: exception raised when file can not be read or written to
    """
    try:
        with open(pizza_toppings_file, 'r', encoding='utf-8') as input_file:
            reader_orders = csv.reader(input_file)
            next(reader_orders) # read past header row
            todays_date = date.today().strftime("%Y-%m-%d")
            orders_output_file = Path(".") / "data" / f"completed_orders_from_flat{todays_date}.csv"
            with open(orders_output_file, 'w', encoding='utf-8') as output_file:    
                output_file.write(
                    "datetime,customer_fname,customer_lname,pizza_size,"
                    "toppings\n")
                for row in reader_orders:
                    timestamp = row[0]
                    lname = row[1]
                    fname = row[2]
                    size = row[3]
                    toppings_list = row[4].split("|")
                    print(
                        f"completed pizza order: datetime={timestamp}, "
                        f"customer name={fname} {lname}, "
                        f"pizza size={size}, "
                        f"pizza toppings={toppings_list}"
                    ) # end print()

                    toppings_string = '|'.join(toppings_list)
                    output_file.write(
                        f"{timestamp},{fname},{lname},{size},"
                        f"{toppings_string}\n"
                    ) # end write()
                # end for
            # end with
        # end with
    except FileNotFoundError as e:
        print(
            f"!!!!!sorry, file located at '{pizza_toppings_file}' is not found. "
            f"'{e}'. please try again when you get a chance!!!!!"
        ) # end print()
    except IOError as e:
        print(
            f"!!!!!sorry, an I/O error occurred, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!sorry, an unexpected, unhandled exception was encountered, "
            f"{e}!!!!!"
        ) # end print()
# end make_pizza_v2()
        
def get_toppings():
    """
    Prompts for sandwich toppings wanted

    args:
        none

    returns:
        list of sandwich toppings
    
    raises:
        none
    """
    toppings_list = []
    while True:
        topping = get_valid_input(
            "Please enter sandwich topping: "
        ) # end get_valid_input()
        toppings_list.append(topping)
        
        if not is_continue():
            break
        # end if
    # end while
    return toppings_list
# end get_toppings()

def get_sandwich_size():
    """
    Prompts for the sandwich size and validates that only the 'small', 
    'large', and 'x-large' values are entered

    args:
        None

    returns:
        A valid string sandwich size

    raises:
        None
    """
    while True:
        size_input = get_valid_input(
            "Please enter the size of the sandwich: "
        ) # end print()
        
        if size_input.lower() in { "small", "large", "x-large" }:
            break
        else:
            print(
                "!!!!!Sorry, the sandwich size was invalid. please only enter "
                "'small', 'large', or 'x-large values!!!!!"
            ) # end print()
        # end if
    # end while
# end get_sandwich_size()
        
def get_sandwich_request():
    """
    Prompts for sandwich request info and returns a dictionary containing the
    sandwich key/value data

    args:
        none
        
    returns:
        dictionary of sandwich data key/value pairs

    raises:
        none
    """
    sandwich_info_dict = {}
    first_name = get_valid_input("Please enter your first name: ")
    sandwich_info_dict['fname'] = first_name

    last_name = get_valid_input("Please enter your last name: ")
    sandwich_info_dict['lname'] = last_name

    sandwich_type = get_valid_input(
        "Please enter the name of the sandwich: "
    ) # end get_valid_input()
    sandwich_info_dict['type'] = sandwich_type

    sandwich_info_dict['size'] = get_sandwich_size()

    sandwich_toppings_list = get_toppings()
    sandwich_info_dict['toppings'] = sandwich_toppings_list
    return sandwich_info_dict
# end get_sandwich_request()

def create_sandwiches():
    """
    Prompt for user's name, sandwich type, sandwich size, and sandwich toppings.
    Then, create sandwich orders file. Also, writes to the status of each
    sandwich order to the display and an output file.

    args:
        none

    returns:
        none

    raises:
        none
    """
    try:
        todays_datetime = datetime.now()
        date_only = todays_datetime.strftime("%Y-%m-%d")
        time_only = todays_datetime.strftime("%H:%M:%S")
        completed_orders_file = Path(".") / "data" / f"completed_orders_{date_only}.csv"
        with open(completed_orders_file, 'w', encoding='utf-8') as orders_status_file:
            file_header = "date,time,lname,fname,type,size,toppings\n"
            orders_status_file.write(file_header)
            while True:
                sandwich_req_dict = get_sandwich_request()
                print(
                    f"The '{sandwich_req_dict['type']}' is ready for "
                    f"'{sandwich_req_dict['lname']}, "
                    f"{sandwich_req_dict['fname']}'.\n"
                ) # end print()

                toppings_delimited_string = "|".join(sandwich_req_dict["toppings"])
                completed_orders_output = (
                    f"{date_only},"
                    f"{time_only},"
                    f"{sandwich_req_dict['lname']},"
                    f"{sandwich_req_dict['fname']},"
                    f"{sandwich_req_dict['type']},"
                    f"{sandwich_req_dict['size']},"
                    f"{toppings_delimited_string}\n"
                ) # end completed_orders_output 
                orders_status_file.write(completed_orders_output)

                if not is_continue():
                    break
                # end if
            # end while    
        # end with
    except IOError as e:
        print(
            f"!!!!!Sorry, the orders details data could not be written "
            f"successfully to the orders status output file: "
            f"'{completed_orders_file}, {e}.\n"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!I'm sorry an unhandled, unexpected exception was " 
            f"raised, {e}!!!!!"
        ) # end print()
    # end try...except
# end create_sandwiches()
        
def build_profile(applicants_file: Path):
    """
    Builds new student applicant user profiles from the flat file data in the
    'applicant_file' comma delimited flat file

    args:
        applicants_file: filepath of the new student applicants to the college

    returns:
        List of dictionaries of student applicant data

    raises:
        FileNotFoundError: raises an exception if the 'applicants_file' can
        not be found

        IOError: raises an exception if the student data can not be read
        from the 'applicants_file' or written to a file processing status
        output file   
    """
    try:
        todays_datetime = datetime.now()
        date_only = todays_datetime.strftime("%Y-%m-%d")
        time_only = todays_datetime.strftime("%H:%M:%S")
        processed_applicants_file = (
            Path(".") / "data" / "out_files" / f"processed_applicants_{date_only}.csv"
        ) # end process_applicants_file

        with open(applicants_file, 'r', encoding='utf-8') as input_file, \
             open(processed_applicants_file, 'w', encoding='utf-8') as output_file:
            output_file.write(
                "process_date,process_time,app_date,lname,fname,email,major,"
                "minor\n"
            ) # end write()
            reader_applicants = csv.DictReader(input_file)
            for row in reader_applicants:
                dt_object = (
                    datetime.strptime(row["timestamp"], '%Y-%m-%dT%H:%M:%S')
                ) # end dt_object

                extracurrs_lst = row["extra_curriculars"].split("|")
                extracurrs_str = ", ".join(extracurrs_lst).title()
                hobbies_lst = row["hobbies"].split("|")
                hobbies_str = ", ".join(hobbies_lst).title()
                print(
                    f"Application processing completed for =>\n"
                    f"Last name: {row['lname'].title()}\n"
                    f"First name: {row['fname'].title()}\n"
                    f"Email: {row['email']}\n"
                    f"Direct messaging: {row['dm']}\n"
                    f"Linked-In: {row['linked_in']}\n"
                    f"Veteran: {row['veteran'].title()}\n"
                    f"Major: {row['major'].title()}\n"
                    f"Minor: {row['minor'].title()}\n"    
                    f"Extracurricular activities: {extracurrs_str}\n"
                    f"Hobbies: {hobbies_str}\n"
                ) # end print()
                output_file.write(
                    f"{date_only},{time_only},"
                    f"{dt_object.year}-{dt_object.month}-{dt_object.day},"
                    f"{row['lname']},{row['fname']},{row['email']},"
                    f"{row['major']},{row['minor']}\n"
                ) # end write()
            # end for
        # end with
    except FileNotFoundError as e:
        print(
            f"!!!!!sorry, file located at '{applicants_file}' is not found. "
            f"'{e}'. please try again when you get a chance!!!!!"
        ) # end print()
    except IOError as e:
        print(
            f"!!!!!sorry, an I/O error occurred, {e}!!!!!"
        ) # end print()
    except Exception as e:
        print(
            f"!!!!!sorry, there was an unhandled, unexpected error that "
            f"occurred, '{e}'!!!!!"
        ) # end print()
    # end try...except
# end build_profile()