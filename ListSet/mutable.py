#list mutable & tuple immutable

my_str = "Hello World!"
print(type(my_str))
print(id(my_str))
print(my_str[1])
# my_str[1] = "o"
print(my_str)
#so string location is also immutable

my_num = 76
print(type(my_num))
print(id(my_num))

my_num = 38
print(id(my_num))

#so the variable my_num is immutable because the value and the memory address both are changed

my_list = [1, 2, 3, 4]
print(my_list)
my_list[1] = 0
print(my_list)
my_tuple = (1, [9, 7, 4], 3, 4)
print(my_tuple[1])
my_tuple[1][2] = 6
print(my_tuple[1])