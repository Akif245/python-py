x=10
print(x)
def my_fcn():
    global x
    x=3  
    y=5
    print(y)
my_fcn()
print(x)
    