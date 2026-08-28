#WAF to print the length of a list. ( list is the parameter)
def length_list(list1):
    result=len(list1)
    return result

print(length_list([1,2,3,4,5]))

#WAF to print the elements of a list in a single line. ( list is the parameter)
def print_list(list2):
    for i in list2:
        print(i,end=' ')

print_list(['apple','dragon fruit','pineapple'])

#WAF to find the factorial of n. (n is the parameter)

def factorial(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    return fac

print(f'Factorial is: {factorial(5)}')

#WAF to convert USD to NPR

def currency_converter(dollar):
    result=dollar*100
    return result

print(f'Result is {currency_converter(100)} NPR')

##Recursive function
#FACTORIAL using recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

# Write a recursive function to calculate the of first n natural numbers. 

def sum_natural_num(n):
    if n==0:
        return 0
    else:
        return n + sum_natural_num(n-1)

print(sum_natural_num(6))

#Write a recursive function to print all elements in a list

def print_list(list1,ind=0):
    if ind==len(list1):
        return

    print(list1[ind],end=' ')
    print_list(list1,ind+1)

print_list(['apple','pineapple','grapes'])