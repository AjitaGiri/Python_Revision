# Write a Program to input 2 numbers & print their sum
num1=int(input('Enter a number: '))
num2=int(input('Enter next  number: '))
sum=num1+num2
print(f'The sum is {sum}')

# WAP to input side of a square & print its area
side= int(input('Enter the length of a square: '))
area= side**2
print(f"The area of square is {area} ")

#WAP to input 2 floating point numbers & print their average.
num1= float(input('Enter a number: '))
num2= float(input('Enter next number: '))
average=(num1+num2)/2
print(f'The average of two numbers is {average:.2f}')

'''WAP to input 2 int numbers, a and b. 
Print True if a is greater than or equal to b. If not print False'''
a=int(input('Enter a number: '))
b= int(input('Enter a number: '))
if a>=b:
    print('True')
else:
    print('False')