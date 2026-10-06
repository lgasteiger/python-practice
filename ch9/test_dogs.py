"""
module name: test_dogs.py

description:
    This unit test file test instances of type Dog. It will call the getters,
    setters, sit(), and roll_over() functions.store a name and an age.

author: LGG
created: 2026-08-04
last modified: 2026-08-04
version: 1.0.0

dependencies:
    None

license:
    None

notes:
    this module contains examples from the "Python Crash Course, 3rd Ed." from
    Prof. Matthes, E.
"""

from dog import Dog

########################
# Main app starts here #
########################
print("**********Test instantiation of a Dog object**********")
my_dog = Dog('Lucky', 10)
print(f"My dog's name is '{my_dog.name}'.\n")
print(f"My dog's age is: '{my_dog.age}'.\n")
your_dog = Dog('Lucy', 5)
print(
    f"Your dog's name is '{your_dog.name}', and she is '{your_dog.age}' " 
    f"years old.\n"
) # end print()

print("**********Test Dog methods**********")
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()
