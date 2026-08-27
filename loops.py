#sum of even numbers
'''
n=int(input('enter a number:'))
total=0
for i in range(1,n+1):
    if i%2==0:
        total+=i
print("Print sum of even numbers: ",total)

#multiplication table printer
n=int(input('Enter a number: '))
print(f"MULTIPLICATION TABLE OF {n} ")
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

#reverse a string uing loop
input_string='QUALITY'
reversed_string=''
for char in input_string:
    reversed_string= char+ reversed_string
print(reversed_string)


#given a string, find the first non-repeated character
input_string='tweet'
for char in input_string:
  # print(input_string.count(char))
     if input_string.count(char)==1:
        print(char)
        break

#compute the factorial of a number using while loop
n=5
i=1
fac=1
while i<=n:
    fac=fac*i
    i+=1
print(f'Factorial of {n} is {fac}')

#keep asking the user for input until they enter a number between 1 and 10

while True:
    num=int(input("enter a number: "))
    if num>=1 and num<=10:
        break
'''
# check if a number is prime
num=int(input('Enter a number: '))
if num>1:
    for i in range(2,num):
        if num%i == 0:
            print('Not Prime')
            break
    else:
        print('Prime')
else:
    print('Not a prime')

#check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate
items=['apple','banana','orange','apple','mango','mango']
unique_items=[]
for item in items:
    if item in unique_items:
        print('Duplicate:',item)
    else:
        unique_items.append(item)
#print(unique_items)