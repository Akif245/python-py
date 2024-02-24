import random

operator =["+","-","*"]
min_operand=3
max_operand=10
def gen_problem():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    
    op=random.choice(operator)
    exp=str(left) +" "+ op +" "+ str(right)
    ans=eval(exp)
    return exp,ans
exp,ans=gen_problem()
print(exp,ans)
                      # or  1 more method without using eval() fcn in p4.py