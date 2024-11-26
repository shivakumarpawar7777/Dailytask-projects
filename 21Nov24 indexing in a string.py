#Indexing in a string 
# -7,-6,-5,-4,-3,-2,-1  (negetive indexing)
# P   r  a  e  e  n  a  (name)
# 0   1  2  3  4  5  6  (positive indexing)

name = "praveena"
print(name[0])
print(name[6])
print(name[-8])

name = "shivakumar"
print(name[0])
print(name[5])
print(name[-8])
print("-----------------------------------------------------------------------------")

#slicing  print(name[startingidex : endindex])
name = "shivakumar"
print(name[0:1+5])
print(name[0:10])
print(name[0:5])
print(name[5:10])
print("------------------------------------------------------------------------------")
 
 #veriablename    print(name[startingidex : endindex : step])
numbers = '1234567890'
print(numbers[0:10:2])
print(numbers[0:10:3])
print(numbers[1:10:4])
print(numbers[2:10:5])
print("-----------------------------------------------------------------------------------")

# Membership checking in string
# in and not in 
a = "hello wecome to world of Python"
aa = "Python"
print(aa in a)
print(a in aa)
print(a and aa)
print(aa and a)

a = "hello wecome to world of Python"
aa = "java"
print(aa in a)
print(a in aa)
print(a and aa)
print(aa and a)
print("-------------------")

a = "hello wecome to world of Python"
aa = "Python"
if aa in a:
    print("aa is available in a ")
if aa not in a:
    print("aa is not available in a ")

a = "hello wecome to world of Python"
aa = "java"
if aa in a:
    print("aa is available in a ")
if aa not in a:
    print("aa is not available in a ")
print("-------------------------------------------------------------------------------------------------")

# removing space from string
#strip()              
username = "shivakumar "
print(len(username))    # to find out the user length 
aa = username.strip()
print(aa)
print(len(aa))

#rstrip() :- rigth side spece 
username = " praveen "
print(len(username))    # to find out the user length 
bb = username.rstrip()
print(bb)
print(len(bb))

#lstrip() :- leftside spece 
username = " ramkumar "
print(len(username))    # to find out the user length 
cc = username.lstrip()
print(cc)
print(len(cc))
print("-=-------------------------------------------------------------------------------------------------")

#replace 
s = "hello wecome to world of Python"
sp = s.replace(" ","")
print(sp)

s = "hello wecome to world of Python"
sp = s.replace("Python","")
print(sp)

s = "hello wecome to world of Python"
sp = s.replace("Python","java")
print(sp)

