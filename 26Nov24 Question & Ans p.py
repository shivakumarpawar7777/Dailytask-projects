"""#1. Python Program to count occurrence of a given characters in string.  
name = "qwertyuiopasdfghjklzxsjdgfiuenkjsdiueyfqiwfnchjfiayfcvbnmplmoknuhvygvtfcrdxesxqazsdfghjgfxcvbjgf"
print(name.count("f")) # to find a perticulau characters how many times available.
print("------------------------------")

#2. Python Program to check if two Strings are Anagram.
a = input("enter the first string: ")
b = input("enter the second strong: ")
if sorted(a) == sorted(b):
    print("both strings are anagram")
else:
    print("not anagram")  
print("------------------------------")

#3. Python program to check a String is palindrome or not. 
z = input("Enter a string: ") 
revstr = z[::-1]
if revstr == z:
    print("palindrome")
else:
    print("Not palindrome")
print("------------------------------")

#4. Python program to replace the string space with a given character.  
s = "hello wecome to world of Python"
sp = s.replace("Python","java")
print(sp)

#5. Python program to replace the string space with a given character using replace() method.  
s = "hello wecome to world of Python"
sp = s.replace("Python","java")
print(sp)
print("------------------------------")
 
#6. Python program to convert lowercase char to uppercase of string. 
z = "Hello wecome to world of Python"  
print(z.upper())
print(z.isupper())
print("------------------------------")
#7. Python program to convert lowercase vowel to uppercase in string.  
s = input("Enter a string: ")
res = 'aeiou'
for i in s:
    if i in res:
        upr = i.upper()
        str = s.replace(i, upr)
print("After converting : ", str) 

#8. Python program to separate characters in a given string.  
string = "hello"
a = list(string)
print(a)
print("-=-------------------------------------------------------------------------------------------------")

#9. Python program to remove blank space from string. 
username = " ramkumar "
print(len(username))    # to find out the user length 
cc = username.lstrip()
print(cc)
print(len(cc))
print("-=-------------------------------------------------------------------------------------------------")

#10. Python program to concatenate two strings using join() method.  
strings = ["Hello", "World"]
a = " ".join(strings)
print(a)  
print("----------------------------")

#11. Python program to concatenate two strings without using join() method.  
s1 = "Hello"
s2 = "World"
z = s1 + " " + s2
print(z)
print("-=-------------------------------------------------------------------------------------------------")

#12. Python program to remove repeated character from string.  
a = {1,2,3,4,5,6,6,5,4,2} 
print(list(set(a))) 
print("The type of data",type(a)) 
print("------------------------------")

#15. Python program to delete vowels in a given string.  
string = input("Enter a string: ")
vowels = "aeiouAEIOU"

result = ""

for char in string:
    if char not in vowels:
        result += char
print(result)
print("------------------------------")

#17. Python program to print the highest frequency character in a String.  

s = "lerarnrirnrgr"
print(s.count("g"))
d = {}
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] =1
print(max(d.values()))
print(max(d, key=d.get))
print("------------------------------")


#21. Python program to calculate sum of integers in string.  
str = input("Enter a string: ")
sum = 0
for i in str:
    if i.isdigit():
        sum = sum + int(i)
print("Total sum in string : ", sum)
print("------------------------------")

#24. Python program to check given character is vowel or consonant. 
name = input("Enter your letter: ")
name = name.lower()
if (name == "a" or name == "e" or name == "i" or name == "o" or name == "u"):
    print("it is a vowel")
else:
    print("consonant")
print("------------------------------")

#25. Python program to check given character is digit or not.
z = "1234567890"   
print(z.isdigit()) 

z = "asdfghj567890"   
print(z.isdigit()) 

z = "asdfghjk"   
print(z.isdigit()) 
print("------------------------------")"""




#16. Python program to count the Occurrence Of Vowels & Consonants in a String.  


 
#18. Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.  

s = "hello wecome to world of Python"
sp = s.replace("h","-")
print(sp)

#19. Python program to count alphabets, digits and special characters.  

#20. Python program to check given character is digit or not using isdigit() method.  

#22. Python program to print all non repeating character in string.  
 
#23. Python program to copy one string to another string.  


