a= int(input("Enter the value of a\n"))
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
     print("Incorrect value")
finally:
    print("Done")