# finding of substring in main string 
#find()  :- return index position on substring in main string.
s = "Hello wecome to world of Python"
print(s.find("world"))
print(s.find("H"))
print(s.find("l"))
print(s.find("n"))
print(s.find("w"))
print(s.find("P"))
print("------------------------------------------------------------------------------")

#index()   :- return index position on substring in main string.
ss = "Hello wecome to world of Python"
print(ss.index("world"))
print(ss.index("H"))
print(ss.index("l"))
print(ss.index("n"))
print(ss.index("w"))
print(ss.index("P"))
print("------------------------------------------------------------------------------")

#split()
z = "Hello wecome to world of Python"  # all word spece = 31. & all word = 6
print(len(z))
za = z.split()
print(len(za))
print(za)

z = "Hello wecome to world of Python"  
print(len(z))
za = z.split("o")
print(len(za))
print(za)

z = "Hello wecome to world of Python"  
print(len(z))
za = z.split("l")
print(len(za))
print(za)

z = "Hello wecome to world of Python"  
print(len(z))
za = z.split("y")
print(len(za))
print(za)
print("------------------------------------------------------------------------------")

#join()   :- @#$%^&*|?><:0 we can user anything
a = "Hello wecome to world of Python"  
js =" ".join(a)
print(len(js))
print(js)

a = "Hello wecome to world of Python"  
js ="_".join(a)
print(len(js))
print(js)

a = "Hello wecome to world of Python"  
js ="*".join(a)
print(len(js))
print(js)
print("------------------------------------------------------------------------------")

#Checking case of a string & Checking type of charectors or string 
# uppre() & isupper()  :- converts all charectors into uppsercase
z = "Hello wecome to world of Python"  
print(z.upper())
print(z.isupper())

z = "HELLO WECOME TO WORLD OF PYTHON"
print(z.upper())
print(z.isupper())
print("---------------------------------")

# lower() & islower()  :- converts all charectors into lowercase
x = "Hello wecome to world of Python"  
print(x.lower())
print(x.isupper())

y = "hello wecome to world of python"
print(y.lower())
print(y.islower())
print("---------------------------------")

# titile() & istitile()    :- converts first into each word
z = "Hello wecome to world of Python"  
print(z.title())
print(z.istitle())

x = "Hello Wecome To World Of Python"
print(x.title())
print(x.istitle())
print("---------------------------------")

# capitalize()   :- converts first charector into uppercase
z = "Hello wecome to world of Python"  
print(z.capitalize())
#print(z.iscapitalize())      we do not have iscapitalize()
print("---------------------------------")

# swapcase()   :- converts all lowercase into uppercase and uppercase into lowercase
z = "HELLO WECOME TO WORLD OF PYTHON"  
print(z.swapcase())

z = "hello wecome to world of python"  
print(z.swapcase())
print("---------------------------------")

#isdigit()
z = "1234567890"  
print(z.isdigit())

z = "asdfghj567890"  
print(z.isdigit())

z = "asdfghjk"  
print(z.isdigit())
print("---------------------------------")

#isalnum()
z = "hello"  
print(z.isalpha())

z = "ASDFG567890"  
print(z.isalpha())

z = "asdf@#$%3456"  
print(z.isalpha())
print("---------------------------------")

#isspase()
z = " "  
print(z.isspace())

z = "asdfghj567890"  
print(z.isspace())

z = "hello"  
print(z.isspace())
print("---------------------------------")


# Checking first & last part of a string 
"""we have 2 type of metheds
1. stratwith()
2. endwith()
EX :- """
email = "shivupawar90@gmail.com"
webside = "wwww.python.com"

print(webside.startswith("www"))
print(email.endswith("com"))
