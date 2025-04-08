class Person:
    def __init__(self, name):
        self.name = name
    @classmethod
    def sayHi(cls):
        print("Hi")

x = Person("Serhii")
x.sayHi()