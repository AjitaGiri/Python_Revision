#WAP to ask the user to enter names of their 3 favorite movies & store them in a list
movie1= input('enter a movie: ')
movie2= input('enter a movie: ')
movie3= input('enter a movie: ')
movies= [movie1,movie2,movie3]

#WAP to check if a list contains a palindrome of elements.
list1=[1,2,2,1]

reverselist1= list1[::-1]
if list1==reverselist1:
    print('True')
else:
    print('False')

'''
WAP to count the number of students with the “A” grade in the following tuple.
[”C”, “D”, “A”, “A”, “B”, “B”, “A”] '''

list_grade=['D','C','A','A','B','B','A']
count_A=list_grade.count('A')
print(count_A)
