n = int(input("Enter the value of n = "))

number_list = list(range(1, n+1))

for i in number_list:
    if i >= 3:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    else:    
        print(i)