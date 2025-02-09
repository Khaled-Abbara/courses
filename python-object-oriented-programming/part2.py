#------------------------------------------------------------

# Encapsulation
# restricting direct access to some of the object's components, 
# usually by making attributes private or protected 
# and providing public methods (getters and setters) to access or modify them.

# class BadBankAccount:
#     def __init__(self, balance):
#         self.balance = balance

# account1 = BadBankAccount(100)
# account1.balance = -1
# print(account1.balance)

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0.0

#     @property
#     def balance(self):
#         return self.__balance
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}, New balance: {self.__balance}")
#         elif amount == 0:
#             print("You didn't deposit any money")
#         elif amount < 0:
#             print("Amount is negative")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}, New balance: {self.__balance}")
#         elif amount == 0:
#             print("You didn't withdraw any money")
#         elif amount < 0:
#             print("Amount is negative")

# account2 = BankAccount()
# account2.deposit(100)
# account2.withdraw(50)

# account2.deposit(0)
# account2.withdraw(-500)
# account2.deposit(-500)     
     
#------------------------------------------------------------

# Abstraction
# Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object.
# We focus on what the object does instead of how it does it.
# this is called "black box design".

# class EmailService:
#     def __init__(self):
#         pass

#     def _connect(self):
#         print("Connecting to email server...")

#     def _authenticate(self):
#         print("Authenticating...")

#     def _disconnect(self):
#         print("Disconnecting...")

#     def send_email(self):
#         self._connect()
#         self._authenticate()
#         print("Sending email...")
#         self._disconnect()


# email = EmailService()
# email.send_email()

#------------------------------------------------------------

# Inheritance


