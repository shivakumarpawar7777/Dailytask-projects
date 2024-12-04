"""#1. Python Program to count occurrence of a given characters in string.  
name = "qwertyuiopasdfghjklzxsjdgfiuenkjsdiueyfqiwfnchjfiayfcvbnmplmoknuhvygvtfcrdxesxqazsdfghjgfxcvbjgf"
print(name.count("f")) # to find a perticulau characters how many times available.
print("---------------1---------------")

#2. Python Program to check if two Strings are Anagram.
a = input("enter the first string: ")
b = input("enter the second strong: ")
if sorted(a) == sorted(b):
    print("both strings are anagram")
else:
    print("not anagram")  
print("--------------2----------------")

#3. Python program to check a String is palindrome or not. 
z = input("Enter a string: ") 
revstr = z[::-1]
if revstr == z:
    print("palindrome")
else:
    print("Not palindrome")
print("----------------3--------------")

#4. Python program to replace the string space with a given character.  
s = "hello wecome to world of Python"
sp = s.replace("Python","java")
print(sp)
print("-----4-------------------------")

#5. Python program to replace the string space with a given character using replace() method.  
s = "hello wecome to world of Python"
sp = s.replace("Python","java")
print(sp)
print("-----------5-------------------")
 
#6. Python program to convert lowercase char to uppercase of string. 
z = "Hello wecome to world of Python"  
print(z.upper())
print(z.isupper())
print("----------------6--------------")

#7. Python program to convert lowercase vowel to uppercase in string.  
s = input("Enter a string: ")
res = 'aeiou'
for i in s:
    if i in res:
        upr = i.upper()
        str = s.replace(i, upr)
print("After converting : ", str) 
print("-=--------------------7-----------------------------------------------------------------------------")

#8. Python program to separate characters in a given string.  
string = "hello"
a = list(string)
print(a)
print("-=------------------------------8-------------------------------------------------------------------")

#9. Python program to remove blank space from string. 
a = "wellcome to my world"
aa = a.replace (" ","")
print(aa)
print("-=-------------9------------------------------------------------------------------------------------")

#10. Python program to concatenate two strings using join() method.  
a = "Python" 
s = "program"
print(" ".join([a,s])) 
print("------------------10----------")

#11. Python program to concatenate two strings without using join() method.  
s1 = "Hello"
s2 = "World"
z = s1 + " " + s2
print(z)
print("-=------------------------11------------------------------------------------------------")

#12. Python program to remove repeated character from string.  
a = {1,2,3,4,5,6,6,5,4,2} 
print(list(set(a))) 
print("The type of data",type(a)) 
print("---------12---------------------")

#13 = 24
#14 = 25 

#15. Python program to delete vowels in a given string.  
string = "PrepInsta"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]
print("\nAfter removing Vowels: ", result)
print("----------15--------------------")

#16. Python program to count the Occurrence Of Vowels & Consonants in a String.  
str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0

for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
print("-----------16-------------------")

#17. Python program to print the highest frequency character in a String.  

a = "GeeksforGeeks"
s = max(a, key=lambda x: a.count(x))
print(s)
print("-----------17-------------------")

#18. Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.  
s = "An apple A day keeps doctor Away."
s = s.replace('a', '$')
print(s)
print("-----------18-------------------")

#19. Python program to count alphabets, digits and special characters.  
s = "praveen@12345"
dig = 0
chrc = 0
spch =0
for char in s :
    if char.isalpha() :
        chrc = chrc+1
    elif char.isdigit() :
        dig = dig+1
    else :
        spch = spch +1
 
print("charectors- ", chrc)
print("digits -", dig)
print("specialsymbals - ", spch)
print("---------19---------------------")

#20. Python program to check given character is digit or not using isdigit() method.  
s = "12345"
print(s.isdigit())  

s2 = "1234a5"
print(s2.isdigit())
print("--------------20----------------")

#21. Python program to calculate sum of integers in string.  
str = input("Enter a string: ")
sum = 0
for i in str:
    if i.isdigit():
        sum = sum + int(i)
print("Total sum in string : ", sum)
print("--------------21----------------")

or
s = "praveen1234"
count = 0
for char in s:
    if char.isdigit():
        count = count + int(char)
    else :
        pass
print(count)
print("-----------21-------------------")

#22. Python program to print all non repeating character in string.  
S = "Ppyytthhoonn"
for i in S:
    count = 0
    for j in S:
        if i == j:
            count+=1
        if count > 1:
            break
    if count == 1:
        print(i,end = " ")
print("--------------22----------------")

#23. Python program to copy one string to another string.  
s = input("Please Enter Your Own String : ")
a = s
r = s[:]
print("The Final String : a  = ", a)
print("The Final String : r  = = ", r)
print("-------------23-----------------")

#24. Python program to check given character is vowel or consonant. 
l = ['a', 'e', 'i', 'o', 'c'] 
if chr in l: 
	print(chr, "is a vowel") 
else: 
	print(chr, "is a consonant")
print("---------------#13 = 24---------------")

#25. Python program to check given character is digit or not.
z = "1234567890"   
print(z.isdigit()) 

z = "asdfghj567890"   
print(z.isdigit()) 

z = "asdfghjk"   
print(z.isdigit()) 
print("----------------#14 = 25 --------------")"""

