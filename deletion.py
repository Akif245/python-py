from array import *
x=int(input("Enter x value\n"))
def  index(arr,x):
    for i in range(5):
         if(arr[i]==x):
            break
            if(i==5):
                print(5)
    for j in range(i):
        arr[j]=arr[j+1]
        print(4)             
arr  = array('i',[1,2,3,4,5])
index(arr,x)