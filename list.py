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
print(list)"""

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
print(list[::-1])
