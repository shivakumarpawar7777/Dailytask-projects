#Write a program to create a set.
set = {1, 2, 3, 4, 5}
print(type(set))

set = {}
print(type(set))
print(set)

#Write program to iterate over sets.
set = {'a', 'b', 'c', 'd'}
for i in set:
    print(i)

#Write a Python program to add member to a set.
set = {1, 2, 3, 4, 5}
set.add(6)

#Write a Python program to remove item from a given set.
set = {1, 2, 3, 4, 5, 6, 7}
set.remove(6)
set.remove(7)
print("element removed from set:",set)

#Write a python program to create a intersection of set ?
set1={1,2,3,4,5}
set2={4,5,6,7,8}
intersection_set = set1.intersection(set2)
print("After intersection:",intersection_set)

#Write a python program to createa unionof set ?
set1={1,2,3,4,5}
set2={4,5,6,7,8}
union_set = set1.union(set2)
print("union of two sets:",union_set)

#Write a python program to create set differance ?
set1={1,2,3,4,5}
set2={4,5,6,7,8}
difference_sets = set1.difference(set2)
print("difference in set:",difference_sets)

#Write a python program to create a symmetric defferance ?
set1={1,2,3,4,5}
set2={4,5,6,7,8}
symmetricdifference_sets = set1.symmetric_difference(set2)
print("After symmetric difference of sets:",symmetricdifference_sets)

#write a python program to find max and min values in a set?
set = {1,2,3,4,5,6,7,8,9}
maximum_value = max(set)
minimum_value = min(set)
print("maximum value of set:",maximum_value)
print("minimum value of set:",minimum_value)

#Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
set1={1,2,3,4,5}
set2={4,5,6,7,8}
difference_update_sets = set1.difference(set2)
print("Difference upadated in first set:",difference_update_sets)

#Write a Python program to remove items 10, 20, 30 from the following set at once.?
set ={10,20,30,40,50,60}

for element in [10,20,30]:
    set.remove(element)
print("After removing elements from set:",set)

#Check if two sets have any elements in common. If yes, display the common elements?
set1={1,2,3,4,5}
set2={4,5,6,7,8}
commom_elements = set1.intersection(set2)

if element:
    print("common elements exist:",commom_elements)
else:
    print("No common elements")

#Update set1 by adding items from set2, except common items?
set1={1,2,3,4,5}
set2={4,5,6,7,8}
common_items = set1.union(set2)
print("updated sets:",common_items)

#Remove items from set1 that are not common to both set1 and set2?
set1={1,2,3,4,5}
set2={4,5,6,7,8}
commom_elements= set1.intersection(set2)
print("Not Common:",commom_elements)

#Write a python program to  add a key to a dictionary ?
dict = {"name" :"ravi", "age" :25}
dict["city"]="hyd"
print("After add key to dictionary:",dict)

#Write a python program to check weather the given value is present in the dictionary or not ?
dict = {'name': 'ravi', 'age': 25, 'city': 'hyd'}
value = "ravi"

if value in dict.values():
    print("value present in dictionary:",value)
else:
    print("value not present in dictionary")
    
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
d={}
for i in range(1,15+1):
    d[i] = i ** 2

print("squares of the keys:",d)

#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
#Write a python program to create a dictionary from the string ?
string1 = "hello world"
char_count = {}

for char in string1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("char count in dictionary:",char_count)

#Write a python program to combine two dictionaries by adding values of common keys ?
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 35}

combined_dict = dict1.copy()

for key, value in dict2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value
print("Combined Dictionary:", combined_dict)

#Write a python program to merge two python dictionaries ?
dict1 = {"a": 10, "b": 20}
dict2 = {"b": 30, "c": 40}

dict1.update(dict2)
print("Merged Dictionary:", dict1)

#Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
string1 = 'skywavessoftwares'
char_count = {}
for char in string1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("char count in dictionary:",char_count)
