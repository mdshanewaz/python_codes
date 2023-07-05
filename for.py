my_list = ["apple", "orange", "Mango", "Lichi"]

for f in my_list:
    print(f)

print("")
print("")

for i in range(1, 10):
    if i > 5:
        break

    print(i)

print("")
print("")


for i in range(1, 10):
    if i > 5 and i < 8:
        continue

    print(i)