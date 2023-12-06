class math:
    def __init__(self,num):
        self.num= num
    def add(self,n):
        self.num=self.num+n
    @staticmethod
    def addition(a,b):
        return a+b
a=math(5)
print(a.num)
        