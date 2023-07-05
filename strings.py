# user_name = "Sha Newaz"

# print(type(user_name)) #type is a class, can pass arrgument

# print(user_name)
# print(user_name.upper()) #upper is method, cannot pass arrgument
# print(user_name.lower()) #lower is also a method like upper

# wcl_text = "hello java. I am coding in java. java is good!!!"
# print(wcl_text.replace("java", "python"))

# print(wcl_text.replace("!", "*", 1))

# vegitable = "Tomato, Capsicum, Garlic, Bokly, Cabage"

# veg_list = vegitable.split(", ")

# print(veg_list)

# cars = "BMW AUDI TOYOTA MARCEDIS ROLSROYS"

# print(cars.split(" "))


#slice a string
# user_name = "Shah Newaz"

# #string_var[start: end]
# first_name = user_name[:4]
# last_name = user_name[5:]

# print(first_name)
# print(last_name)


# #Cocatenate
# fname = "Shah"
# lname = "Newaz"

# u_name = fname + " " + lname
# print(u_name)


# wc_msg = "Welcome to our site"

# complect_wc_msg = wc_msg + " " + user_name

# print(complect_wc_msg)


#formate method 
# f_name = "Shah"
# l_name = "Newaz"
# u_id = 122

# full_name = "{first_name} {last_name}'s user ID is {user_ID}".format(
#     first_name = f_name, 
#     last_name = l_name, 
#     user_ID = u_id
#     )
# print(full_name)

print("{0}, I am {1}".format("Hello", "Shawon"))
print("{var} is an {1} and also a {0}".format(
    "learner", 
    " engineer",
     var = "Shawon"
    ))

#escape sequence use \
print("Teacher is a \"Good boy\"")
