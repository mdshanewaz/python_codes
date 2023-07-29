class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return "My name is {}".format(self.name)


class Student(Person):
    def __init__(self, name, age, dept):
        self.dept = dept
        Person.__init__(self, name, age) 

student_one = Student("Shawon", 26, "ICE")
print(student_one.introduce())


class A:
    def __init__(self):
        print("From class A")

class B():
    def __init__(self):
        print("From class B")

class C(B):
    def __init__(self):
        print("From class C")
        B.__init__(self)



class D(A):
    def __init__(self):
        print("From class D")
        A.__init__(self)
        B.__init__(self)
        

object_d = D()
        
