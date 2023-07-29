class A:
    def __init__(self):
        print("From Class A")

class B(A):
    def __init__(self):
        print("From Class B")
        super().__init__()

    def my_method(self):
        print("This is Class B")

class C(B):
    def __init__(self):
        print("From class C")
        super().__init__() 
    
    def my_method(self):
        print("This is Class C")

class D(C, B):
    def __init__(self):
        print("From class D")
        super().__init__()

obj_D = D()

