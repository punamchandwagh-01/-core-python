# 1 What is self in Python:--> self refers to the current object.

class Demo:
    def show(self):
        print("Hello")

# 2 What is __init__():-->It is a constructor that runs automatically when an object is created.

class Person:
    def __init__(self, name):
        self.name = name
 #       
