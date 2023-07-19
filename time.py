import time

print(time.time())

second = 1689784818.0904508
print(time.ctime(second))

print("line 1")
time.sleep(3)
print("line after 3s")

print(time.localtime(second))