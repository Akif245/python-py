def fcn():
    try:
        list =[1,2,3,4,5]
        i = int (input("Enter the value i"))
        print([i])
        return 1
    except:
        print("Error")
        return 0
    finally:
        print("Always Executed")
x = fcn()
print(x)