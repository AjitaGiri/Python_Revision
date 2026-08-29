'''Create a new file “practice.txt” using python. Add the following data in it: 
Hi everyone
we are learning File I/O
using Java. 
I like programming in Java.'''

with open('practice.txt','w') as f:
    f.write('Hi everyone. ' \
    'We are learning File I/O using Java. ' \
    'I like programming in Java')


#WAF that replace all occurrences of “java” with “python” in above file
def replace_java():
    with open('practice.txt','r') as f:
        data=f.read()

    new_data= data.replace('Java','python')

    with open('practice.txt','w') as f:
        f.write(new_data)

replace_java()

#Search if the word “learning” exists in the file or not.
def check_for_learning():
    with open('practice.txt','r') as f:
        data=f.read()
        if 'learning' in data:
            print('Learning exists')
        else:
            print('Learning does not exist')

check_for_learning()

#WAF to find in which line of the file does the word “learning”occur first. Print -1 if word not found.
def check_for_line():
    data=True
    line_no=1
    with open('practice.txt','r') as f:
        while True:
            data=f.readline()

            if data== '':
                break

            if 'learning' in data:
                print(line_no)
                return
            line_no+=1
    print(-1)

check_for_line()

#From a file containing numbers separated by comma, print the count of even numbers

count=0
with open('numbers.txt','r') as f:
    data=f.read()
    number=data.split(',')

    for nums in number:
        nums=int(nums)

        if nums%2==0:
            count+=1
    print(count)

