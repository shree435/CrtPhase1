class Student:
    def write(self):
        print("Students write")
class Student1(Student):
    def write(self):
        print("Student1 writes record")
class Student2(Student):
    def write(self):
        print("Student2 writes assignment")
class Student3(Student):
    def write(self):
        print("Student3 writes exam")
class Student4(Student):
    def write(self):
        print("Student4 writes notes")
obj=Student2()
obj.write()