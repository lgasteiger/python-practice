"""
filename: favorite_languages.py

author: gasteiger, Lg
version: 1.0 
"""

def get_language(dic_name, dic_key):
    """
    this function returns the language value of dic_name[dic_key]
    """
    return dic_name[dic_key].title()
# end get_language()

def get_lang_keys(dic_name):
    """
    this function will print only the keys of the programming language's keys
    """
    for name in dic_name.keys():
        print(name.title())
    # end for
# end get_lang_keys()
        
def check_friend_keys(dic_name):
    """
    this function will determine if certain friends are "keys" in the dic_name
    Python 3 dictionary data structure and print the friends in sorted order
    to the screen 
    """
    curr_friends = ['phil', 'sarah']

    for friend_name in sorted(dic_name.keys()):
        print(f"hi {friend_name.title()}")

        if friend_name in curr_friends:
            fav_lang = dic_name[friend_name].title()
            print(
                f"\t{friend_name.title()}, i see you love the {fav_lang} " +
                f"programming language!"
            ) # end print()
        # end if
            
        if friend_name not in curr_friends:
            print(f"{friend_name.title()}, please retake our poll")
        # end if
    # end for
# end check_friend_keys(dic_name)
            
def print_fav_lang_values(prog_lang_dict):
    """
    this function will print the current friends' programming languages to
    the screen
    """
    print("the following programming languages have been mentioned:")
    for language in prog_lang_dict.values():
        print(language.title())
    # end for
# end print_fav_lang_values()

def print_unique_fav_langs(prog_lang_dict):
    """
    this funcion will print only unique data values in the prog_lang_dict to
    the screen
    """
    for language in sorted(set(prog_lang_dict.values())):
        print(language.title())
    # end for
# end print_unique_fav_langs()

############################
# main program starts here #
############################
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
} # end favorite_languages dictionary

print("*****test the get function to return a dictionary value*****")
language = get_language(favorite_languages, 'sarah')
print(f"Sarah's favorite langauge is: '{language}'")
print()

print("*****test built-in dictionary get() method*****")
fav_lang = favorite_languages.get('jen', 'sorry, no team member with that name').title()
print(f"Jen's favorite language is: '{fav_lang}'")
fav_lang = favorite_languages.get('Lg', 'sorry, no team member with that name').title()
print(f"Lg's favorite language is: '{fav_lang}'")
print()

print("*****test printing dictionary keys only*****")
get_lang_keys(favorite_languages)
print()

print("*****test working with dictionary keys comparisons*****")
check_friend_keys(favorite_languages)
print()

print("*****test the Python 3 dictionary values function*****")
print_fav_lang_values(favorite_languages)
print()

print(
    "*****test the friends' programming languages dictionary with the set()" +
    "function to prevent duplicate data values from appearing on the screen" +
    "******"
) # end print()
print_unique_fav_langs(favorite_languages)
print()
