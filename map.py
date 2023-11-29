# simple fcn for cube
def cube(x):
    return x*x*x
print(cube(4))
l=[1,2,3,4,5,6]
newl=list(map(cube,l))
print(newl)
# maps are also called "Higher Order" fcn
# they takes function itself as argument
 
#        by lamda fcn

l=[1,2,3,4,5]
newl=list(map(lambda x:x*x*x,l))
print(newl)