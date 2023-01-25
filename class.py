class Student:
    name='Sweety'
    def __init__(self,name):
        print("Obj created")
        print(name)
        print(self.name)
        self.name=name
        print(name)
s1=Student("Srivalli")