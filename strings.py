user_name = "Sha Newaz"

print(type(user_name)) #type is a class, can pass arrgument

print(user_name)
print(user_name.upper()) #upper is method, cannot pass arrgument
print(user_name.lower()) #lower is also a method like upper

wcl_text = "hello java. I am coding in java. java is good!!!"
print(wcl_text.replace("java", "python"))

print(wcl_text.replace("!", "*", 1))

vegitable = "Tomato, Capsicum, Garlic, Bokly, Cabage"

veg_list = vegitable.split(", ")

print(veg_list)

cars = "BMW AUDI TOYOTA MARCEDIS ROLSROYS"

print(cars.split(" "))