import random

operator =["+","-","*"]
min_operand=3
max_operand=12
total_problem=10


def gen_problem():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    
    op=random.choice(operator)
    exp=str(left) +" "+ op +" "+ str(right)
    ans=eval(exp)
    return exp,ans

for i in range(total_problem):
    exp,ans=gen_problem()
    while True:
        guess=input("Problem #" + str(i+1) + " : " + exp + " = ")
        if guess == str(ans):
            break