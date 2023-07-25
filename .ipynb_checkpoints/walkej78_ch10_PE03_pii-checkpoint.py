# define Pii class for walkej78_ch10_PE03_pii.py
class Pii:
    # initilize module that holds the following personal data: name, address, age, and phone number
    def __init__(self, name, address, age, phone_num):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_num = phone_num
    
    # set_name This method assigns a value to the __name field.
    def set_name(name):
        name = self.__name
        
    # set_address This method assigns a value to the __address field.
    def set_address(address):
        address = self.__address
        
    # set_age This method assigns a value to the __age field.
    def set_age(age):
        age = self.__age
        
    # set_phone_num This method assigns a value to the __phone_num field.
    def set_phone_num(phone_num):
        phone_num = self.__phone_num
        
    # get_name This method assigns a value to the __name field.
    def get_name(self):
        return self.__name
    
    # get_address This method assigns a value to the __address field.
    def get_address(self):
        return self.__address
    
    # get_age This method assigns a value to the __age field.
    def get_age(self):
        return self.__age
    
    # get_phone_num This method assigns a value to the __phone_num field.
    def get_phone_num(self):
        return self.__phone_num
    