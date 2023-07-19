def Student(std):
    std = std
    print("Welcome Mr", std)

std1 = Student('Shawon')

std2 = Student('Sazzad')

def user_info(fname, lname):

    print("Hello {}".format(fname))
    print("His last name is {}".format(lname))
    print("His full name is {} {}".format(fname, lname))


user_info("Shah", "Newaz")

user_info(lname="Waliullah", fname="Shah")

def calculate_vat(price, percent=5):
    total_pay = price + price*(percent/100)

    print("total proce is", total_pay)

retu1 = calculate_vat(200)
rest2 = calculate_vat(100, 10)

def square(a):
    return a**2

def cube(a):
    return a*a*a

def avg(a, b):
    return (a+b)/2

sqr = lambda a : a*a
print(sqr(2))

avr = lambda a, b: (a+b)/2
print(avr(4, 6))  
