# Importing all the Files from the Menu1 Module 
from Menu import *
# We use the Tabulate Module to design the Tables and the Menu's
from tabulate import tabulate
class Dashboard:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def options (self):
        #  Designing the admin menu
        print("*"*120)
        print("WELCOME TO ONE STOP FAST FOODS")   
        print("*"*120)   
        
    #    Using Tabulate to display the menu with Customer Login
        print(tabulate([['1', 'User Login'], ['2', 'Exit']], headers=['S/N', 'Options']))
       
        option=int(input("Enter your Option:"))
        
        if option == 1:
            print("User Login")
            self.username = input("Enter username: \n")
            self.password = input("Enter password: \n")
            if self.username == "user" and self.password == "using":
                # print("Welcome to our restaurant")
                print("Pleasure Having you!!")
                customer = Customer()
                customer.Tables()
                print("Thank you for visiting us")
                exit()
            else:
                print("Invalid username or password")
                self.options()
        
       