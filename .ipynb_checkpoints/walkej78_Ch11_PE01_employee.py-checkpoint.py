# class file to walkej78_Ch11_PE01_employee.py
class Employee:
    # initialize Employee class
    def __init__(self, employee_name, employee_number):
        # define employee_name attribute
        self.__employee_name = employee_name
        # define employee_number attribute
        self.__employee_number = employee_number
    
    # define set_employee_name to set an employee's name
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    # define set_employee_number to set an employee's number
    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number
    
    # define get_employee_name to retrieve an employee's name
    def get_employee_name(self):
        return self._employee_name
    
    # define get_employee_number to retrieve an employee's number
    def get_employee_number(self):
        return self.__employee_number

# create subclass ProductionWorker
class ProductionWorker:
    # initialize ProductionWorker subclass
    def __init__(self, employee_name, employee_number, shift_number, hr_pay_rate):
        # define shift_number attribute
        self.__shift_number = shift_number
        # define hr_pay_rate attribute to represent hourly pay rate
        self.__hr_pay_rate
    
    # define set_shift_number for two integers (1 and 2) to represent the day shift as 1 and the night shift as 2.
    def set_shift_number(self, shift_number):
        self.__shift_number = int(shift_number)
        
    # define set_hr_pay_rate to set an employee's hourly pay rate
    def set_hr_pay_rate(self, rate):
        self.__hr_pay_rate = float(rate)
        
    # definte get_shift_number to retrieve an employee's shift number
    def get_shift_number(self):
        return self.__shift_number
    
    # define get_hr_pay_rate to retrieve an emplployee's hourly pay rate
    def get_hr_pay_rate(self):
        return self.__hr_pay_rate