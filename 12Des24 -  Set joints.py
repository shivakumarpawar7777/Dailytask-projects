# set joint 
#Union() : it will return both the S1 and S2 valus
s1 = {2,3,4,9,0,6}
s2 = {1,2,3,4,5,6,7,8}
print(s1.union(s2))

#intersection : return common elements form the both sets.
s1 = {2,3,4,9,0,6}
s2 = {1,2,3,4,5,6,7,8}
print(s1.intersection(s2))

#difference() : return s1 that values are present in 
s1 = {2,3,4,9,0,6}
s2 = {1,2,3,4,5,6,7,8}
print(s1.difference(s2))

# system defference : return both s1 & s2 but not in both sets
s1 = {2,3,4,9,0,6}
s2 = {1,2,3,4,5,6,7,8}
print(s1.symmetric_difference(s2))

# decleration : 

d = {}
print(type(d))

d["name"] = "shiv"
d["age"] = "27"
d["salery"] = "500000"

d["name"] = "shivakumar" # it will update element
d["agee"] = "27"
print(d)
print("-----------------------------")

# accesing data 
d["name"] = "shiv"
d["age"] = "27"
d["salery"] = "500000"

print(d["name"])
ad = d.get("age")
print(ad)   #or
print("-----------------------------")

print(d)
for i in d:
    print(i, d[i])