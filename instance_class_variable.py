class employee:
    # this is "class variable"
    companyname="apple"
    def __init__(self,name) :
        self.name=name
# this is a instance variable
        self.raise_amount=200 
    def showdetail(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyname} is {self.raise_amount}")
emp1=employee("Akif")
emp1.raise_amount=300
emp1.showdetail()
emp2=employee("Ahmed")     
emp2.showdetail()
        