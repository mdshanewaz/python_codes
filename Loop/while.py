i = 1

while i <= 10:
    if i == 5:
        print("Stop")
        break
    print(i)
    i += 1

print("outside the 1st loop")
print("")
print("")


j = 1

while j < 10:
    j += 1
    if j > 5 and j < 8:
        print("Skipping")
        continue

    print(j)
    

print("outside the 2nd loop")