"""Function in python
#Function :- block of code excecutes whenever we call it. (reused block code)

#Arguments:- information or data passed to the function as a arguments , which specifies after function name.

S = input("enter your string: ")   
re = s.replace(" ", "$")                     
"""
# Besic syntax of function
"""def functionname (formala argument):
    pass
functionname(actual argument)"""

"""def space_replece(s):
    rs = s.replace(" ", "$")   
    print(rs)
S = input("Enter your input hare: ")
space_replece(s)    """

# python function to print even as a list?

def get_evens(x):
    l = []
    for i in x:
        if i % 2 == 0:
            l.append(i)
    print(i)
l1 = [0,2,1,11,13,14,20,15,16,18,17,19,10]
get_evens(l1)  

#four type of arguments
#1.positinal arguments
#2.Keyword arguments
#3.Variable lenth argument
#4.Keyword variable length
#1.positinal arguments:- assing arguments to the function
def find_greatest(x,y):
    if x > y:
        print(x,"is greater")
    else:
        print(y, "is greater")

x = 20
y = 30
find_greatest(x,y)
print("----------")

def sum(x,y):
    print(x + y)
    print(x - y)

x = 20
y = 30
sum(x,y)
print("----------")

#2.Keyword arguments:- 
def sum(a,b):
    print(a + b)
    print(a - b)

x = 20
y = 30
sum(a=x,b=y)
print("----------")

def sum(b,a):
    print(a + b)
    print(a - b)

x = 20
y = 30
sum(a=x,b=y)
print("----------")

def greet(name, msg):
    print("Hi", name, msg)

name = "Shivakumr pawar"
msg = "Good morning"
greet(name,msg)  # greet(name=name, msg=msg)

#3.Variable lenth argument:- we can number of argument to the functon.
def sum(*n):
    total = 0
    for i in n:
        total = total + i
    print(total)

sum(10,20,30,40,50)
sum(1,2,3)
sum(1,1)

#4.Keyword variable length

def student_data(**n):
    print(n)
student_data(m=36, p=67, c=76, e=80)    

print("-------------")

def student_data(**n):
    print(n)
    for k,v in n.items():
        print(k," = ",v)    
student_data(m=36, p=67, c=76, e=80) 

# defualt argument 
def greet(name, msg):
    print("Hi", name, msg)

name = "Shivakumr pawar"
msg = "Good morning"
greet(name,msg)  # greet(name=name, msg=msg)
