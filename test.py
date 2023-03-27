
import math

# quadratic equation and solution

a = int(input())
b = int(input())
c = int(input())
D = math.sqrt(b*b - 4*a*c)

x1 = (-b+D)/2*a
x2 = (-b-D)/2*a

print(x1)
print(x2)

# swapping two variables without 3rd variable

a = a-b
b = a+b
a = b-a

print("a", a)
print("b", b)

