#list :- is buit in data type that can stores set of values like (int, float, string ..etc)
# And its a mutenle data type.
# []
"""marks = [1, 2, 3, 4, 5, 6.5,"shiv"]
print(type(marks))
print(len(marks))
print(marks[1])
print(marks[-1])

#list slicing 
print(marks[1:7])
print(marks[0:2])
print(marks[1:-1])
print(marks[2:5])
print("-------------------------------")"""

"""#list methods:- Ordering of list
#append() :- (list.append())adds one element at the time
list = [1,3,4,2,5,7,6]
list.append(8)
print(list)

list = [1,3,4,2,5,7,6]
list.append("shiv")
print(list)
print("-------------------------------")

#sort() :- (list.sort())sort in ascending order 
list = [1,3,4,2,5,7,6]  #OUTPUT:- [1, 2, 3, 4, 5, 6, 7]
list.sort() 
print(list)

list = ['a', 'c', 'd', 'b', 'e']  #output :- ['a', 'b', 'c', 'd', 'e']
list.sort() 
print(list)
print("-------------------------------")

list = [1,3,4,2,5,7,6]
list.sort("shiv")             # we cannot use a string 
print(list)

#reverse() :- list.reverse()
list = [1, 3, 4, 2, 5, 7, 6, 8]    #OUT PUT :- [8, 6, 7, 5, 2, 4, 3, 1]
list.reverse()
print(list)

list = ['a', 'c', 'd', 'b', 'e']  
list.reverse() 
print(list)
print("-------------------------------")

#reverse using slice
list = "hello my name is shiv"     #OUT PUT :- vihs si eman ym olleh
print(list[::-1])

list = "what you what od"    #assinment 1Q #OUT PUT :- do tahw uoy tahw
print(list[::-1])

list = "od tahw uoy tnaw"    #assinment 2Q #OUT PUT :- want you what do
print(list[::-1])"""

# aliasing & cloning
data = "student data"
data_copy = "studnt data"

x = [1, 2, 3, 4, 5]
y = x
print(id(x))
print(id(y))

y[1] = 20
print(id(x))
print(id(y))
print("----------------------------------")
# cloning >>> slicing 
a = [20, 30, 40, 50]
b = x[:]
print(id(a))
print(id(b))

b[1] = 200
print(id(a))
print(id(b))
print("----------------------------------")

# comporing of two list
x = [1, 2, 3, 4, 5, 6]
y = [1, 3, 5, 7 , 9, 6]

print(x > y)
print(y > x)
print(x < y)
print(y < x)


x = ["ram", "shiv", "jay"]
y = ["kiran", "sai", "ABC"]
print(x > y)
print(y > x)
print(x < y)
print(y < x)

x = ["A", "B", "C"]
y = ["a", "b", "c"]
print(x > y)
print(y > x)
print(x < y)
print(y < x)
print("----------------------------------")

#memberchip cheking list
l = [1, 2, 3, 4, 5, 6]
print(2 in l)
print(10 not in l)

# Nestet list
l = [1,2,3,[4,5,6,[7,8,9]]]
print(l[3])
print(l[3][3])
print(l[3][3][2])

