from abc import ABC,abstractmethod
class Teacher(ABC):
    @abstractmethod
    def teach(self):
        pass
    def correct(self):
        pass
class Teacher1(Teacher):
    def teach(self):
        print("Teacher1 teaches Python")
    def correct(self):
        print("Teacher1 corrects mid papers")
class Teacher2(Teacher):
    def teach(self):
        print("Teacher2 teaches C")
    def correct(self):
        print("Teacher2 corrects sem papers")
class Teacher3(Teacher):
    def teach(self):
        print("Teacher3 teaches Java")
    def correct(self):
        pass
obj=Teacher3()
obj.correct()
obj.teach()