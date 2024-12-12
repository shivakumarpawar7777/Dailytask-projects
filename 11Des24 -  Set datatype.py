#set data type 
s = {1,2,3,"set",2.2,3,4,5,6,True}
print(type(s))

s = {}
print(type(s))  #class 'dict'
print(s)

s = {1,2,3,"set",2.1,3,4,5,6,True,False}  # duplicate values are not allowed.
print(s)  # ! = true

# accesing 
s = {1,2,3,"set",2.1,3,4,5,6,True,False}  # intexing is not possible in set
#print(s[1])

#Adding element to the set
s = {"shiv", "rama", "praven", "kishan"}
s.add("venkat")
print(s)
print(type(s))

# updata()
s = {1,2,3,"set",2.1,3,4,5,6,True,False}  
s1 = {"shiv", "rama", "praven", "kishan"}
s.update(s1)
print(s)

#Removing element to the set
s = {1,2,3,"set",2.1,3,4,5,6,True,False}  
s1 = {"shiv", "rama", "praveen", "kishan"}
s1.remove("praveen")
print(s1)

s1.remove("rama")
print(s1)

# discard()
s1 = {"shiv", "rama", "praveen", "kishan"}
s1.discard("zzzz")
print(s1)

s1.discard("praveen")
print(s1)
print("---------------")

# pop() : it will remove anythin from output
s1 = {"shiv", "rama", "praveen", "kishan"}
s1.pop()
print(s1)
print("---------------")


# clear
s1 = {"shiv", "rama", "praveen", "kishan"}
s1.clear()
print(s1)
print("---------------")
