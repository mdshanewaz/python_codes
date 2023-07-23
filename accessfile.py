import os
import pathlib

path = '../Folder1/'
all_files = os.listdir(path)

for files in all_files:
    if os.path.isfile(os.path.join(path, files)):
        print("{} is a file".format(files))

all_files2 = os.scandir(path)

for file in all_files2:
    print(file)

for file in all_files2:
    if file.is_file():
        print("{} is a file".format(file.name))

path_object = pathlib.Path(path)
for file in path_object.iterdir():
    print(file)
    if file.is_file():
        print(file.name)
