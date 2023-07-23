# file = open('read_fl.py', 'r')
# print(file.read())

# file.close()

#When we use open() method/function we must use the close() method/function as well. Other wise it will reserver some memory to it. Otherwise use with open() method/function.

with open('read_fl.py', 'r') as file:
    print(file.read())