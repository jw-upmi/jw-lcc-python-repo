# class file to walkej78_Ch11_PE02_employee.py
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
        return self.__employee_name
    
    # define get_employee_number to retrieve an employee's number
    def get_employee_number(self):
        return self.__employee_number

# create subclass ProductionWorker
class ProductionWorker(Employee):
    # initialize ProductionWorker subclass
    def __init__(self, employee_name, employee_number, shift_number, hr_pay_rate):
        # call the superclass __init__ method
        Employee.__init__(self, employee_name, employee_number)
        # define shift_number attribute
        self.__shift_number = int(shift_number)
        # define hr_pay_rate attribute to represent hourly pay rate
        self.__hr_pay_rate = float(hr_pay_rate)
    
    # define set_shift_number for two integers (1 and 2) to represent the day shift as 1 and the night shift as 2.
    def set_shift_number(self, shift_number):
        self.__shift_number = int(shift_number)
        
    # define set_hr_pay_rate to set an employee's hourly pay rate
    def set_hr_pay_rate(self, hr_pay_rate):
        self.__hr_pay_rate = float(hr_pay_rate)
        
    # definte get_shift_number to retrieve an employee's shift number
    def get_shift_number(self):
        return self.__shift_number
    
    # define get_hr_pay_rate to retrieve an emplployee's hourly pay rate
    def get_hr_pay_rate(self):
        return self.__hr_pay_rate

# create subclass ShiftSupervisor
class ShiftSupervisor(Employee):
    # initialize ShiftSupervisor subclass
    def __init__(self, shift_number, annual_salary, annual_production_bonus):
        # call the superclass __init__ method
        Employee.__init__(self, shift_number, employee_name, employee_number)
        # define shift_number attribute
        self.__shift_number = int(shift_number)
        # define annual_salary attribute
        self.__annual_salary = float(annual_salary)
        # define annual_production_bonus attribute
        self.__annual_production_bonus = float(annual_production_bonus)
        
    # define set_shift_number for two integers (1 and 2) to represent the day shift as 1 and the night shift as 2.
    def set_shift_number(self, shift_number):
        self.__shift_number = int(shift_number)

    # define set_annual_salary to set annual salary for shift supervisor
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = float(annual_salary)
    
    # definte set_annual_production_bonus to set annual production bonus for shift supervisor
    def set_annual_production_bonus(self, annual_production_bonus):
        self.__annual_production_bonus = float(annual_production_bonus)

    # definte get_shift_number to retrieve an employee's shift number
    def get_shift_number(self):
        return self.__shift_number
    
    # definte get_annual_salary to retrieve annual salary for shift supervisor
    def get_annual_salary(self):
        return self.__annual_salary
    
    # define get_annual_production_bonus to retrieve annual production bonus for shift supervisor
    def get_annual_production_bonus(self):
        return self.__annual_production_bonus