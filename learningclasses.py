


class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('connor', 'fryar', 50000)
emp_2 = Employee('colleen', 'fryar', 60000)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))



'''
emp_str_1 = 'john-doe-70000'
emp_str_2 = 'steve-smith-30000'
emp_str_3 = 'jane-doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
'''
'''
first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
'''

'''
# Employee.set_raise_amount(1.05)
emp_1.set_raise_amount(1.05)
# effects both class and instance in both ways

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
'''
"""
class methods v instance methods
"""


'''
class variables vs instance variables.
print(Employee.num_of_emps)

'''
'''
# print(Employee.__dict__)
# print(emp_1.__dict__)

Employee.raise_amount = 1.05
print(emp_1.raise_amount)
# universally changes the raise_amount
'''
'''
emp_1.raise_amount = 1.05
print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# changing the raise for an instance 
# changes the __dict__ of the instance
# changes the value just for that instance
'''
'''print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# looks to gind if the class contains the element
# instance looks to see if the class contains the element
'''
'''
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
'''
'''
# emp_1.raise_amount
# Employee.raise_amount
'''
'''
end of video one

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())

'''
'''
Manual ===

Note fullname() needs a self due to the fact that it 
implicitly gains the instance that it is used on
emp_1.fullname() will error without 
fullname(self)

Employee.fullname(emp_1) does the same thing as:
emp_1.fullname()

print('{} {}'.format(emp_1.first, emp_1.last))


emp_1.first = 'connor'
emp_1.last = 'fryar'
emp_1.email = 'connorfryar@gmail.com'
emp_1.pay = 50000

emp_2.first = 'colleen'
emp_2.last = 'fryar'
emp_2.email = 'colleenfryar@gmail.com'
emp_2.pay = 60000
'''