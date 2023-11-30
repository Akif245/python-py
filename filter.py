#  filter is also a "higher order fcn"
l = [1,2,3,4,5,6,7,8,9]
def fcn(a):
    return a>6
new = list(filter(fcn,l))
print(new)