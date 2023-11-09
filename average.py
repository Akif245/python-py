def average(*number):    
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    return sum/len(number)
ans=average(2,2,2)
print(ans)







    