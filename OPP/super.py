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


class User:

    def __init__(self, name, total):
        self.name = name
        self.total = total

    def get_shipping_cost(self):
        if self.total > 1000:
            return 40
        return 60


class Premium(User):

    def get_discount(self):
        if self.total > 2000:
            return 100
        return 20

    def get_shipping_cost(self):
        return 0

preium_user = Premium("Shawon", 2000)
normal_user = User("Test_user", 100)

print(preium_user.get_shipping_cost())
print(normal_user.get_shipping_cost())