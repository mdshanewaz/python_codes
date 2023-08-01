#function as a parameter in function
def my_fun():
    print("Hello World!")

def another_funct(func):
    func()
    print("This is from print function")

another_funct(my_fun)


#nested fun
def greet(name):
    def hello():
        return "Hello my name is " + name
    return  hello

VAR = greet("Shawon")
print(greet)
print(greet("Shawon"))

#use decorator
def great(fun):
    def inner():
        fun()
        print("This is form inner of great")
    return inner

@great
def hellio():
    print("This is hellio function")

print(hellio())

print(great)
great(hellio)
