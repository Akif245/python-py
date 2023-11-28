a=int(input("Enter value between 0 and 6\n"))
if (a<0 or a>6 ):
    print("yes")
    raise ValueError("wrong value")