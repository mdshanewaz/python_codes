class Person:
    instution_name = "IT and Software"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        return "My name is {}".format(self.name)

    @classmethod
    def get_inst_name(cls):
        return cls.instution_name
    
print(Person.get_inst_name(), "\n")

persoon_1 = Person("Shawon", 26, "Male")
print(persoon_1.name)
print(persoon_1.age)
print(persoon_1.gender)
print(persoon_1.introduce())
print("\n")

persoon_2 = Person("Rimi", 24, "Female")
print(persoon_2.name)
print(persoon_2.age)
print(persoon_2.gender)
print(persoon_2.introduce())
print("\n")

