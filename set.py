# sets : Are collection of defined object
s1={1,2,3,4,5,"akif"}
print(type(s1))
s2={1,2,3,"hi"}
print(s1.union(s2))
print(s1.intersection(s2))
s3=s1.symmetric_difference(s2)
print(s3)
print(s1.isdisjoint(s2))
s1.add("hello")
print(s1)
s1.remove("akif")
print(s1)
s1.pop()
print(s1)
del s1