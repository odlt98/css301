#Omar De La Torre
#5/2/2019

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def myfunc(self):
        print("Welcome " + self.name) 

p1 = Student("Omar", "Computer Science")
p1.myfunc()

p1.major = "Criminal Justice"

print(p1.name)
print(p1.major)

    
