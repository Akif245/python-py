# "this dir fcn shows all the atributes, methods etc."
a=[1,2,3,4,5,6,7,8,9,10]
print(dir())
print(a.__add__)

# "This dict fcn shows all the arguments used  in the fcn "
class person:
    def __init__(self,name,age,version):
        self.name=name
        self.age=age
        self.version=version
p=person("Akif",18,2.0)
print(p.__dict__)
        
# this provides Documentation for the class
print(help(person))

