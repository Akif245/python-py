class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showdata(self):
        print(f"The name of employee:{self.id} is {self.name}")
class programmer(employee):
    def showlanguage(self):
        print("The default language is python")
        
e=employee("Akif",100)            
e.showdata()
e1=programmer("Akf",100)       
e1.showlanguage()     
        
        