'''You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.
”python”, “java”, “C++”, “python”, “javascript”,
“java”, “python”, “java”, “C++”, “C”
'''
list1=['python','java','C++','python','javascript','java','python','java','C++','C']
subject_unique=set()
for x in list1:
    if x not in subject_unique:
        subject_unique.add(x)
print(f'the total number of classrooms needed is {len(subject_unique)}')

#Print numbers from 1 to 100. 
i=1
while i<=100:
    print(i)
    i+=1

#Print numbers from 100 to 1. 
i=100
while i>=1:
    print(i)
    i-=1

#Print the multiplication table of a number n. 
n=int(input('Enter a number: '))
print(f'Multiplication table of {n} is: ')
i=1
while i<=10:
    print(f'{n}*{i}={n*i}')
    i=i+1
#for i in range (1,11):
#    print(f'{n}*{i}={n*i}')

#Print the elements of the following list using a while loop: 
list1=[1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
i=0
while i<len(list1):
    print(list1[i])
    i+=1

#Search for a number 49 in this tuple using while loop:
list2=[1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
i=0
while i<len(list2):
    if list2[i]==49:
        print(f"{list2[i]} found at {i} index")
    i+=1

#WAP to find the sum of first n numbers. (using while
n=5
total=0
i=1
while i<=n:
    total=total+i
    i+=1
print("Sum is: ",total)

#WAP to find the factorial of first n numbers. (using for)
n=5
fac=1
for i in range(1,n+1):
    fac=fac*i
print(f'Factorial of {n} is: {fac}')