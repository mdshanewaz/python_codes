my_dict = {
    "name": "Shawon", 
    "relagion": "Islam", 
    "skills": ("Python", "JavaScript", "C++"),
}

print(my_dict["skills"])
print(my_dict.get("Age"))

my_dict["name"] = "Test user"
print(my_dict["name"])

my_dict.update(
    {
        "name": "Shah Newaz",
        "Skills": ("C++", "Python", "JavaScript"),
    }
)
print(my_dict)

my_dict["Age"] = 26
print(my_dict)

my_dict.update(
    {
        "Address" : "Feni",
    }
)
print(my_dict)

# del keyword
del my_dict["Age"] 
print(my_dict)

# pop method
my_dict.pop("Address")
print(my_dict.pop("name"))
print(my_dict)