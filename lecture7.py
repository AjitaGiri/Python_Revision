#Create a student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def print_average(self):
      average= (self.marks1+self.marks2+self.marks3)/3
      print(f'The average marks is {average:.2f}')

s1=Student('Jake',89,92,88)
s1.print_average()

#Create Account class with 2 attributes- balance & account no.
#Create methods for debit, credit & printing the balance

class Account:
   
   def __init__(self,balance,account_no):
      self.balance=balance
      self.account_no=account_no

   def debit(self,amount):
      self.balance-=amount
      print(f'{amount} was debited')
      print(f'total balance: {self.print_bal()}')

   def credit(self,amount):
      self.balance+=amount
      print(f'{amount} was credited')
      print(f'total amount = {self.print_bal()}')
   def print_bal(self):
      return self.balance

acc1=Account(500,123)
acc1.debit(100)
acc1.credit(500)
      
      