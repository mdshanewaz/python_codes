file = open("words.txt", "r")

while True:
    line = file.readline()

    if not line:
        break
    print(line)

print(file.readlines())

search_words = ["Python", "C", "OOP", "Hello", "Java", "C++", "PHP"]

import os
print(os.getcwd())