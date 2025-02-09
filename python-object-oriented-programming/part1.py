#------------------------------------------------------------

# everything in python is an object

# name = "khaled"
# age = 15

# print(type(name))
# print(type(age))

#------------------------------------------------------------

# A class is a blueprint for creating objects (a particular data structure), 
# providing initial values for state (member variables or attributes), 
# and implementations of behavior (member functions or methods).

# class Dog:
#     def __init__(self, name, breed, owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner

#     def bark(self):
#         print("woof woof")  
    
# class Owner:
#     def __init__(self, name, contact_number):
#         self.name = name
#         self.contact_number = contact_number


# owner1 = Owner("Sally", "123456789")
# doggy = Dog("doggy", "poodle", owner1)
# print(doggy.owner.contact_number)

#------------------------------------------------------------

# this is a recap of the previous example
# I have also shown that Person1 and Person2 are two different objects
# and they have different attributes, and are unique

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old")


# Person1 = Person("Dana", 12)
# Person1.greet()

# Person2 = Person("Ahmad", 19)
# Person2.greet()

#------------------------------------------------------------

# you can include an object inside of another objects method
# you can modify the data of the objecct

# class user:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password

#     def say_hi_to_user(self, user):
#         print(f"sending mesaage to {user.username}: Hi {user.username}! How are you doing? it's me {self.username}")

# user1 = user("khaled123", "cool@gmail.com", "123456")
# user2 = user("FerrySQL", "ferry@gmail.com", "123456")

# user1.say_hi_to_user(user2)

# user2.username = "CoolKarel"

# user1.say_hi_to_user(user2)

#------------------------------------------------------------

# Accessing and modifying Data
# 1. The traditional way: make the data private and create getter and setter methods
# the "concenting adults" philosophy, mean that the user of the class should know what it is doing

# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         # _ prefix means that the variable is private
#         self._email = email
#         self.password = password

#     def get_email(self):
#         return self._email

#     def set_email(self, new_email):
#         self._email = new_email

# user1 = User("khaled123", "khalid@gmail.com", "123456")
# print(user1.get_email())
# user1.set_email("khalooodi@gmail.con")
# print(user1.get_email())

#------------------------------------------------------------

# the double underscore __ prefix means that the variable is private 
# and cannot be accessed because Python will change the name of the variable. 
# these are called Name Mangled variables

# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         # _ prefix means that the variable is private
#         self.__email = email
#         self.password = password

# user1 = User("khaled123", "khalid@gmail.com", "123456")
# print(user1.__email)

#------------------------------------------------------------

# 2. The Pythonic way: use the @property decorator
# The getter and setter properties
# We use @property to add functionality to the variables

# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self._email = email
#         self.password = password

#     @property
#     def email(self):
#         print("getting email...")
#         return self._email

# this is python's way of setting a new value to the variable
# by using the .setter decorator

#     @email.setter
#     def email(self, new_email):
#         if "@" in new_email:
#             print("setting email...")
#             self._email = new_email
#             print(self._email)
#         else:
#             print("Invalid email address")

# user1 = User("khaled123", "khalid@gmail.com", "123456")
# print(user1.email)
# user1.email = "dsadwwadwaa"
# user1.email = "khalidabbara@gmail.com"

#------------------------------------------------------------

# Static attributes / class attributes
# this is an attribute that belongs to the class itself, 
# not any specific instance of the class.

# class User:
#     active_users = 0

#     def __init__(self, username, email, password):
#         self.username = username
#         self._email = email
#         self.password = password
#         User.active_users += 1

# user1 = User("khaled123", "dad@gmail.com", "123456")
# user2 = User("Dana123", "sally@gmail.com", "123456")

# print(User.active_users)

#------------------------------------------------------------

# Static Methods / Class Methods
# Static methods are methods that belong to the class itself rather than its object.
# Static methods are memory efficient because they are only created once and shared among all instances of the class.

# class BankAccount:
#     MIN_BALANCE = 0

#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self._balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited {amount} to {self.owner}'s account")
#             print(f"New balance: {self._balance}")
#         else:
#             print("Invalid amount")
        
#     @staticmethod
#     def is_valid_interest_rate(rate):
#         if 0 <= rate <= 3:
#             print("Valid interest rate")
#             return True
#         else:
#             print("Invalid interest rate")
#             return False


# account1 = BankAccount("Khaled", 400)
# account1.deposit(100)

# print(BankAccount.is_valid_interest_rate(2))
# print(BankAccount.is_valid_interest_rate(4))

#------------------------------------------------------------

