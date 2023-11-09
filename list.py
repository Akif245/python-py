li=["hi","hii"]
l=[1,1,1,1,22,3,43,5,"hlo", True]
print(type(l))
print(len(l))
print(l[2])
print(l[6])
print(l[-3])
if 1 in l:
 print("yes")
else:
    print("no")
                   # to print whole list
print(l[:])
print(l[0:7:3])
a=slice(0,3)
print(l[a])
add=l+li
print(add)
    
    