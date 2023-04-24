# This program prints Hello, world!

print('Hello, world!')

#q: what does SOLID stand for in OO programming
#A: Single responsibility, Open-closed, Liskov substitution, Interface segregation, Dependency inversion
#q: what is the difference between a class and an object
#A: A class is a blueprint for an object. An object is an instance of a class.
#q: what is the difference between a class and a module
#A: A class is a blueprint for an object. A module is a file containing Python definitions and statements.
#q: what is the difference between a class and a package
#A: A class is a blueprint for an object. A package is a collection of modules.
#q: what is the difference between a class and a library
#A: A class is a blueprint for an object. A library is a collection of packages.

#regular expression that matches a valid email address
#A: ^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$

#regular expression that matches a valid UK phone number
#A: ^\+?44\d{10}$

#code to test if a string is a valid email address

import re

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)

print(is_valid_email("ab.com"))
print(is_valid_email("a@b.com"))

#code to test if a string is a valid UK phone number
def is_valid_phone_number(phone):
    return re.match(r"^\+?44\d{10}$", phone)

print(is_valid_phone_number("1234567890"))
print(is_valid_phone_number("+441234567890"))

