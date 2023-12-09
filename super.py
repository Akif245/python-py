class employee:
    def __init__(self,name ,id ):
        self.name=name
        self.id=id
class programmer(employee):
    def __init__(self,name,id,lang):
        
        super().__init__(name,id)
        self.lang=lang
a=employee("Akif",44570)
b=programmer("Akif",123,"python")
print(a.name)
print(a.id)
print(b.lang)
