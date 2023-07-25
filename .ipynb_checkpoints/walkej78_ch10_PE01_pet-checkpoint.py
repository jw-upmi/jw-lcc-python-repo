# define pet class for walkej78_ch10_PE01_pet.py
class Pet:
    # initialize private methods
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # set_name This method assigns a value to the __name field.
    def set_name(self, name):
        self.__name = name
        
    # set_animal_type This method assigns a value to the __animal_type field.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        
    # set_age This method assigns a value to the __age field.
    def set_age(self, age):
        self.__age = age
        
    # get_name This method assigns a value to the __name field.
    def get_name(self):
        return self.__name
    
    # get_animal_type This method assigns a value to the __animal_type field.
    def get_animal_type(self):
        return self.__animal_type
    
    # get_age This method assigns a value to the __age field.
    def get_age(self):
        return self.__age