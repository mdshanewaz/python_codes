import os
import pathlib

path = 'test.txt'
print(os.path.isfile(path))

file = pathlib.Path(path)
print(file.is_file())

