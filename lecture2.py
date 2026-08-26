# WAP to input user’s first name & print its length
name= input("enter user's first name: ")
print(f'the length of username is {len(name)}')

# WAP to find the occurrence of ‘$’ in a String.
fruit='pineapple$apple'
print(fruit.index('$'))
# print(fruit.find('$'))

#WAP to check if a number entered by the user is odd or even
NUM= int(input('Enter a number: '))
if NUM %2==0:
    print("Even")
else:
    print("ODD")

#WAP to find the greatest of 3 numbers entered by the user
num1=  int(input('Enter a number: '))
num2= int(input('Enter a number: '))
num3= int(input('Enter a number: '))
if num1>num2 and num1>num3:
    print(f'{num1} is greatest')
elif num2>num3 and num2>num1:
    print(f'{num2} is greatest')
else:
    print(f'{num3} is greatest')

#WAP to check if a number is a multiple of 7 or not
if num1 % 7==0:
    print(f"{num1} is mutiple of 7")
else:
    print(f"{num1} is not multiple of 7")