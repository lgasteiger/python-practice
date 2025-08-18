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
