file = open('list.py', 'r')

print(file.read())

while True:
    line = file.readline()
    if not line:
        break
    print(line)

all_lines = file.readlines()
print(all_lines)