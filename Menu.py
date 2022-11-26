from abc import ABC, abstractmethod
from tabulate import tabulate

# Creating a class for the Restaurant services
class Services(ABC):
    def __init__(self,):
        self
    # abstract method Choice
    @abstractmethod
    def choice (self):
        pass
    # abstract method Amount
    @abstractmethod
    def setTotal(self):
        pass
    # abstract method GetTotal
    @abstractmethod
    def getTotal(self):
        pass

# Food class and this class inherits from the Services class  
class Food(Services):
    
    def __init__(self):
        super().__init__()
        self.total = 0
        
    # This method is used to get the choice of the customer
    def choice(self,take):
        self.availability = {1: {'name': 'chips and Chicken', 'price': 55000}, 
        2: {'name': 'Masala Chips and Chicken', 'price': 65000}, 
        3: {'name': 'Mashed potatoes and Chicken', 'price': 55000}, 
        4: {'name': 'Plantain and BBQ meat', 'price': 33000}, 
        5: {'name': 'Nyama  Fest pizza and Tomato soup', 'price': 33000}, 
        6: {'name': 'Beef sausage and side salads', 'price': 18000}, 
        7: {'name': 'Potatoes and onion rings', 'price': 14000}, 
}
        if take in self.availability:
            print("You have selected: ",self.availability[take]['name'])
            self.quantity = int(input("Enter the quantity:"))
            self.bill = self.availability[take]['price'] * self.quantity
            self.setTotal(self.bill)
            print("Bill: ",self.getTotal())
            
    # This method is used to Display the menu of the restaurant to the customer
    def Menu(self):
        # Using tabulate to display the menu
         print(tabulate([['1', 'chips and Chicken', '55000'], 
         ['2', 'Masala Chips and Chicken', '65000'], 
         ['3', 'Mashed potatoes and Chicken', '55000'], 
         ['4', 'Plantain and BBQ meat', '55000'], 
         ['5', 'Nyama  Fest pizza and Tomato soup', '33000'], 
         ['6', 'Beef sausage and side salads', '18000'],
            ['7', 'Potatoes and onion rings', '14000']], headers=['S/N', 'Food', 'Price']))
    # This method is used to set the total amount of the customer
    
    def setTotal(self,bill):
        self.total = self.total + bill
        return self.total
    # This method is used to get the total amount of the customer
    def getTotal(self):
        return self.total
 
    # class Drinks and this class inherits from the Services class
class Drinks(Services):
    
    def __init__(self):
        super().__init__()
        self.total = 0
    #  This method is used to get Drink choice of the customer
    def choice (self,take):
        #  This is the dictionary of the available drinks
        self.availability = {1:{'name':'Boosters','price':12000},2:{'name':'Lemonades','price':15000},3:{'name':'Smoothies','price':50000},4:{'name':'AfricanTea','price':15000},5:{'name':'Water','price':3000}}
        # This is used to check if the drink is available in the dictionary of the available drinks
        if take in self.availability:
            # This is used to get the name of the drink and the quantity of the drink
            print("You have selected: ",self.availability[take]['name'])
            self.quantity = int(input("Enter the quantity:"))
            self.bill = self.availability[take]['price'] * self.quantity
            self.setTotal(self.bill)
            # This is used to get the total bill of the customer
            print("Bill: ",self.getTotal())
            
    def Menu(self):
        # Using tabulate to display the menu
        print(tabulate([['1', 'Boosters', '12000'], ['2', 'Lemonades', '15000'], ['3', 'Smoothies', '50000'], ['4', ' AfricanTea', '15000'], ['5', 'Water', '3000']], headers=['S/N', 'Drink', 'Price']))
    def setTotal(self,bill):
        self.total = self.total + bill
        return self.total
    def getTotal(self):
        return self.total
# Customer class and this class inherits from the Drinks and Food class
class Customer(Drinks,Food):
    def __init__(self):
        self.drink = Drinks()
        self.food = Food()
        self.take = 0
        self.apply = 0


    # Getting customers choice  
    def choice(self):
        print("Select the type of service you want")


        # Displaying the menu in the Tabular form
        
        print(tabulate([['1', 'Food'], ['2', 'Drinks']], headers=['S/N', 'Service']))
        self.take = int(input())


        #  To order food or drink
        if self.take == 1:
            print(self.food.Menu())
            self.apply = int(input("Enter your choice : "))
            self.food.choice(self.apply)
            
            # To order for more food or drink
            next = input("Do you want to order more food?,or get a drink (yes/no) : ")
            if next == 'yes':
                self.choice()
  
        elif self.take == 2:
            print(self.drink.Menu())
            self.apply = int(input("Enter your choice : "))
            self.drink.choice(self.apply)
            
            # To order for more drinks or food 
            next = input("Do you want to order more drinks?,or get food (yes/no) : ")
            if next == 'yes':
                self.choice()
        # This method is used to return the Total amount of the customer request
    def Amount(self):
        return self.food.getTotal() + self.drink.getTotal()
    
    
    #This method is used to get the number of people on a table
    def Tables(self):
        summation = 0
        storage = []
        customer = Customer()
        number = int(input("Enter the number of people on the table : "))
        for i in range(number):
            print("Customer ",i+1)
            customer.choice()
            storage.append(customer.Amount())
            length = len(storage)
            for i in range(length):
                summation+=storage[i]
            print("*"*30)
            print ("Total amount to be paid is : ",summation)
            print("*"*30)
        print("Thank you for choosing us")
 