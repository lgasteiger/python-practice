"""
module name: dog.py

description:
    This class represents a dog, and it will store a name and an age. Moreover,
    it will give each instance of a dog the ability to sit and roll over.

author: LGG
created: 2026-08-03
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
class Dog:
    """
    This class represents a dog, and will simply model common dog attributes
    and capabilities. It will store a name and an age, and it will give each 
    instance of a dog the ability to sit and roll over.
    """
    def __init__(self, name, age):
        """
        Constructor of class Dog that will initialize the name and age
        attributes.
        """
        self._name = name
        self._age = age
    # end __init__()

    @property
    def name(self):
        """
        Returns the name of the current object of type Dog.
        """
        return self._name
    # end name() getter

    @name.setter
    def name(self, value):
        """
        Sets the name of current object of type Dog.
        """
        if not isinstance(value, str):
            raise ValueError("!!!!!Value must be a string value!!!!!")
        # end if

        self._name = value
    # end name() setter
    
    @property
    def age(self):
        """
        Returns the age value of the current object of type Dog.
        """
        return self._age
    # end age() getter

    @age.setter
    def age(self, value):
        """
        Sets the age of the current object of type Dog.
        """
        if value < 0:
            raise ValueError("!!!!!Age cannot be negative!!!!!")
        # end if

        self._age = value
    # end age() setter
        
    def sit(self):
        """
        Simulates the current Dog object sitting in response to a command.
        """
        print(f"The dog named '{self._name}' is now sitting.")
    # end sit()
        
    def roll_over(self):
        """
        Simulates the current Dog object rolling over in response to a command.
        """
        print(f"The dog named '{self._name}' is rolling over.")
    # end roll_over()
# end class Dog