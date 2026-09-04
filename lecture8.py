#Single Inheritance
class Car:
    color='red'
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped....")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
        super().start()

car1=ToyotaCar('Fortuner')
car2=ToyotaCar('Prius')
print(car1.color)
car1.start()
car2.stop()

#super() is used to access the method from parent class

## operator overloading

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(f'{self.real}i+{self.img}j')

    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)

c1=Complex(5,6)
c1.showNumber()
c2=Complex(2,1)
c2.showNumber()
c3=c1+c2
c3.showNumber()

#Define a Circle class to create a circle with radius r using the constructor. Compute aread and perimeter
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        print(f'Area of circle is {math.pi*self.radius**2:.2f}')

    def Perimeter(self):
        print(f'Perimeter of circle is {2*math.pi*self.radius:.2f}')

cr1=Circle(7)
cr1.Area()
cr1.Perimeter()

#Define a Employee class with attributes role,department & salary.This class also has showDetails method
# Create an Engineer class that inherits properties from Employee and has additional attributes:name and age

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print(f'Role:{self.role}, Department: {self.dept}, Salary: {self.salary}')


class Engineer(Employee):
    def __init__(self,name,age,role,dept,salary):
        self.name=name
        self.age=age
        super().__init__(role,dept,salary)

emp1=Engineer('Ajita',24,'Frontend Developer','Ecommerce','50,000')
emp1.showDetails()

#Create a class called Order which stores item & its price
# Use dunder function __gt__() to conver that:
#  order>order2 if price of oreder1>price of order2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,other_order):
        return self.price>other_order.price
          
o1=Order('Apple',500)
o2=Order('Banana',200)
print(o1>o2)                        