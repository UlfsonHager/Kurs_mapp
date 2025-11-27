<<<<<<< HEAD
# Bokuppgifter kap 6

import numpy as np

import matplotlib as plt


# Nr 1
a = 10
b = [5, 7, 3]
c = {2, 7, 1, 8, 2, 8}
def my_fun(x):
    return 2*2
d = my_fun


print(type(a))
print(type(b))
print(type(c))
print(type(d))


# Nr 2a

my_var = (1, 1, 3, 5)
print(isinstance(my_var,tuple)) # Ja, det var det

# Nr 2b
print(isinstance(my_var,list)) #Nej, det var det inte

# Nr 3 a-g

class FruitProduct:
    """A class representing fruit products in a store."""
    def __init__(self, price, qty):
        self.price = price
        self.qty = qty
        pass
    
swe_apples = FruitProduct(52, 1)
#print(help(swe_apples)) # Docstring
print(swe_apples) # metodet och attribut, tryck <enter> i konsolen
print(type(swe_apples)) # Skriv ut typen, mm
print(isinstance(swe_apples,FruitProduct)) # True ok ok

# Nr 4
class Square:
    def __init__(self, side_len):
        self.side_len = side_len
        
    def area(self):
        return (self.side_len*self.side_len)
    
    def perimeter(self):
        return(self.side_len*2)
        pass

ret1 = Square(4)
print("Area: ",ret1.area())
print("Perimeter: ",ret1.perimeter())

# Nr 5
# a = Räknar ut medelvärde och antl i en lista, indenteringen är superviktig
class DescribeStat():
    """This is the docString räknar ut div från en lista """
    def __init__(self):
        self.data= []
    
    def add_data(self, data):
        if isinstance(data,list):
            self.data.extend(data)
      
    def calc_sum(self):
        return sum(self.data)
    
    def calc_no_of_elements(self):
        return len(self.data)
    
    def calc_mean(self):
        return (self.__calc_sum__())/(self.calc_no_of_elements())
        
    def print_summary(self):
        print('Sum: ',self.__calc_sum__())
        print('No of elements :',self.calc_no_of_elements())
        print('Mean :',self.calc_mean())
        
        
    
L = [1,2,1,3,5,7,4,9,10,3,2,1,6,4,3,2,1,10,9,1,8,7,3,2,1]

my_data = DescribeStat()
my_data.add_data(L)
my_data.print_summary()

help(my_data)

# Nr 5 b,  Går inte att utöka/ändra en tuple, extend funkar inte, deklareras med () istället



class BankAccount():
    def __init__(self):
        self.account_holder=""
        self.balance=0
        
    def deposit(self, amount): # Sätta in
        self.balance=self.balance+amount
        
    def withdraw(self, amount): # Ta ut
        if self.balance-amount>0:
            self.balance=self.balance-amount
        else:            
            print("Not enought with money")
            
    def print_saldo(self):
        print("Saldo :", self.balance, " kr")
        
bc = BankAccount()
bc.deposit(200)
bc.print_saldo()
bc.deposit(100)
bc.print_saldo() # Nu 300
bc.withdraw(200)
bc.print_saldo() # Nu 100
bc.withdraw(200) # går ej
=======
# Bokuppgifter kap 6

# Nr 1
a = 10
b = [5, 7, 3]
c = {2, 7, 1, 8, 2, 8}
def my_fun(x):
    return 2*2
d = my_fun


print(type(a))
print(type(b))
print(type(c))
print(type(d))


# Nr 2a

my_var = (1, 1, 3, 5)
print(isinstance(my_var,tuple)) # Ja, det var det

# Nr 2b
print(isinstance(my_var,list)) #Nej, det var det inte

# Nr 3 a-g

class FruitProduct:
    """A class representing fruit products in a store."""
    def __init__(self, price, qty):
        self.price = price
        self.qty = qty
        pass
    
swe_apples = FruitProduct(52, 1)
#print(help(swe_apples)) # Docstring
print(swe_apples) # metodet och attribut, tryck <enter> i konsolen
print(type(swe_apples)) # Skriv ut typen, mm
print(isinstance(swe_apples,FruitProduct)) # True ok ok

# Nr 4
class Square:
    def __init__(self, side_len):
        self.side_len = side_len
        
    def area(self):
        return (self.side_len*self.side_len)
    
    def perimeter(self):
        return(self.side_len*2)
        pass

ret1 = Square(4)
print("Area: ",ret1.area())
print("Perimeter: ",ret1.perimeter())

# Nr 5
# a = Räknar ut medelvärde och antl i en lista, indenteringen är superviktig
class DescribeStat():
    """This is the docString räknar ut div från en lista """
    def __init__(self):
        self.data= []
    
    def add_data(self, data):
        if isinstance(data,list):
            self.data.extend(data)
      
    def __calc_sum__(self):
        return sum(self.data)
    
    def calc_no_of_elements(self):
        return len(self.data)
    
    def calc_mean(self):
        return (self.__calc_sum__())/(self.calc_no_of_elements())
        
    def print_summary(self):
        print('Sum: ',self.__calc_sum__())
        print('No of elements :',self.calc_no_of_elements())
        print('Mean :',self.calc_mean())
        
        
    
L = [1,2,1,3,5,7,4,9,10,3,2,1,6,4,3,2,1,10,9,1,8,7,3,2,1]

my_data = DescribeStat()
my_data.add_data(L)
my_data.print_summary()
help(my_data)

# Nr 5 b,  Går inte att utöka/ändra en tuple, extend funkar inte, deklareras med () istället



class BankAccount():
    def __init__(self):
        self.account_holder=""
        self.balance=0
        
    def deposit(self, amount): # Sätta in
        self.balance=self.balance+amount
        
    def withdraw(self, amount): # Ta ut
        if self.balance-amount>0:
            self.balance=self.balance-amount
        else:            
            print("Not enought with money")
            
    def print_saldo(self):
        print("Saldo :", self.balance, " kr")
        
bc = BankAccount()
bc.deposit(200)
bc.print_saldo()
bc.deposit(100)
bc.print_saldo() # Nu 300
bc.withdraw(200)
bc.print_saldo() # Nu 100
bc.withdraw(200) # går ej
>>>>>>> 0e12af3e5bea5bb0d4423cd5a917b131e52781fd
