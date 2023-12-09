class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
ans=shape(7,8)
print(ans.area())
c=circle(9)
print(c.area())