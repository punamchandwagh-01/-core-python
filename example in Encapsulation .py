#  Example in Encapsulation in pyhton


class Student:
    def __init__(self, name, marks):
        self.__marks = marks   # private variable
        self.name = name

    def get_marks(self):
        return self.__marks

    def set_marks(self, m):
        if m >= 0:
            self.__marks = m

s = Student("Rahul", 80)
print(s.get_marks())   # 80
s.set_marks(90)
print(s.get_marks())   # 90
